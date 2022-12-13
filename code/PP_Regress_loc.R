#!/usr/bin/env R

# Title: PP_regress_loc.R
# Author details: Dashing_Dogins
# Date: Nov 2022

#preparation
require(tidyverse)

#input data
MyData <- as.data.frame(read.csv("../data/EcolArchives-E089-51-D1.csv", header = T))

#convert mg to g
#MyDF <- MyData %>% rowwise() %>% mutate(Prey.mass = ifelse(Prey.mass.unit == "mg", Prey.mass / 1000, Prey.mass))

# create variables
MyDF = MyDF %>% 
    mutate(Predator.mass.log = log(Predator.mass),
           Prey.mass.log = log(Prey.mass),
           SizeRatio = Prey.mass / Predator.mass,
           group = as.factor(paste(Type.of.feeding.interaction, Predator.lifestage)))
# regression
result = full_join(
    MyDF %>%
        group_by(Type.of.feeding.interaction, Predator.lifestage, Location) %>%
        group_modify(~ broom::tidy(lm(Predator.mass.log ~ Prey.mass.log, data = .x))) %>% 
        mutate(term = ifelse(term=="Prey.mass.log", "Slope", "Intercept")) %>% 
        ungroup() %>% 
        select(Type.of.feeding.interaction, Predator.lifestage, Location, term, estimate) %>% 
        spread(term, estimate),
    MyDF %>%
        group_by(Type.of.feeding.interaction, Predator.lifestage, Location) %>%
        group_modify(~ broom::glance(lm(Predator.mass.log ~ Prey.mass.log, data = .x))) %>% 
        ungroup() %>% 
        select(Type.of.feeding.interaction, Predator.lifestage, Location, r.squared, statistic, p.value) %>% 
        rename(`F-statistic` = statistic)
)

# save result
write.csv(result, file = "../results/PP_Regress_loc.csv", row.names = FALSE)


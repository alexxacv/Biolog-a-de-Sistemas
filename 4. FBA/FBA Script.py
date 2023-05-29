from __future__ import print_function
import cobra
from cobra import Model, Reaction, Metabolite
model = Model("ejemploFBA")

### Definición de metabolitos ###

### Metabolitos "inventados" ###
A = Metabolite("A", name="A", compartment="C")
B = Metabolite("B", name="B", compartment="C")
C = Metabolite("C", name="C", compartment="C")
D = Metabolite("D", name="D", compartment="C")
E = Metabolite("E", name="E", compartment="C")
F = Metabolite("F", name="F", compartment="C")
G = Metabolite("G", name="G", compartment="C")
H = Metabolite("H", name="H", compartment="C")

### Cofactores y otros productos (considerar cada especie de cofactor) ###
NAD = Metabolite("NAD", name="NAD", compartment="c")
NADH = Metabolite("NADH", name="NADH", compartment="c")
ADP = Metabolite("ADP", name="ADP", formula="C10H15N5O10P2", compartment="c")
ATP = Metabolite("ATP", name="ATP", formula="C10H16N5O13P3", compartment="c")
CO2 = Metabolite("CO2", name="CO2", formula="C102", compartment="c")

### Reacciones de intercambio (medios instra(c) y extracelular(e)) ###

# Entrada de A
reaction = Reaction("A_Tr")
reaction.name = "A_Tr"
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({A: 1.0})
model.add_reactions([reaction])
# Entrada de B
reaction = Reaction("B_Tr")
reaction.name = "B_Tr"
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({B: 1.0})
model.add_reactions([reaction])
# Entrada de E
reaction = Reaction("E_Tr")
reaction.name = "E_Tr"
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({E: -1.0})
model.add_reactions([reaction])
# Entrada de G
reaction = Reaction("G_Tr")
reaction.name = "G_Tr"
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({A: -1.0})
model.add_reactions([reaction])
# Entrada de H
reaction = Reaction("H_Tr")
reaction.name = "H_Tr"
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({A: -1.0})
model.add_reactions([reaction])
# Entrada de CO2
reaction = Reaction("CO2_Tr")
reaction.name = "CO2_Tr"
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({A: -1.0})
model.add_reactions([reaction])

### Reacciones del modelo ###

#v_1: A + ATP ----> C + CO2 + ADP
reaction = Reaction("v_1")
reaction.name = "v_1"
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({A: -1.0, ATP: -1.0, C: 1.0, CO2:1.0, ADP: 1.0})
model.add_reactions([reaction])
#v_2: B + NAD ----> C + NADH
reaction = Reaction("v_2")
reaction.name = "v_2"
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({B: -1.0, NAD: -1.0, C: 1.0, NADH: 1.0})
model.add_reactions([reaction])
#v_3: C + ADP ----> D + ATP
reaction = Reaction("v_3")
reaction.name = "v_3"
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({C: -1.0, ADP: -1.0, D: 1.0, ATP:1.0})
model.add_reactions([reaction])
#v_4: C ----> E + CO2
reaction = Reaction("v_4")
reaction.name = "v_4"
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({C: -1.0, E: 1.0, CO2:1.0})
model.add_reactions([reaction])
#v_5: D + ATP ----> F + CO2 + ADP
reaction = Reaction("v_5")
reaction.name = "v_5"
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({D: -1.0, ATP: -1.0, F:1.0, CO2:1.0, ATP:1.0})
model.add_reactions([reaction])
#v_6: D + NADH ----> G + NAD
reaction = Reaction("v_6")
reaction.name = "v_6"
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({D: -1.0, NADH: -1.0, G:1.0, NAD: 1.0})
model.add_reactions([reaction])
#v_7: F + NADH + ATP ----> H + NAD + ADP
reaction = Reaction("v_7")
reaction.name = "v_7"
reaction.lower_bound = 0.
reaction.upper_bound = 1000.
reaction.add_metabolites({F: -1.0, NADH: -1.0, ATP:-1.0, H: 1.0, NAD: 1.0, ADP:1.0})
model.add_reactions([reaction])

### Flux Balance Analysis ###

model.objective = "v_6"
solution = model.optimize()



#Solution:
    # solution.objective_value (float)
    # solution.fluxes (pandas series, valor de cada flujo v_i)
solution.fluxes

model.metabolites.ATP.summary()


print("%i reactions initially" % len(model.reactions))
print("%i metabolites initially" % len(model.metabolites))
print("%i genes initially" % len(model.genes))
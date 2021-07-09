import numpy as np
from skfuzzy import control as ctrl

temperatura = ctrl.Antecedent(np.arange(0, 38, 1), "Temperatura")
humidade = ctrl.Antecedent(np.arange(0, 101, 1), "Humidade")

potencia = ctrl.Consequent(np.arange(0, 101, 1), "Potência")

temperatura.automf(number=3, names=["Baixa", "Média", "Alta"])
humidade.automf(number=3, names=["Baixa", "Média", "Alta"])
potencia.automf(number=3, names=["Baixa", "Média", "Alta"])

temperatura.view()
humidade.view()
potencia.view()

r1 = ctrl.Rule(temperatura["Baixa"] & humidade["Baixa"], potencia["Alta"])
r2 = ctrl.Rule(temperatura["Baixa"] & humidade["Média"], potencia["Alta"])
r3 = ctrl.Rule(temperatura["Baixa"] & humidade["Alta"], potencia["Média"])

r4 = ctrl.Rule(temperatura["Média"] & humidade["Baixa"], potencia["Baixa"])
r5 = ctrl.Rule(temperatura["Média"] & humidade["Média"], potencia["Baixa"])
r6 = ctrl.Rule(temperatura["Média"] & humidade["Alta"], potencia["Média"])

r7 = ctrl.Rule(temperatura["Alta"] & humidade["Baixa"], potencia["Baixa"])
r8 = ctrl.Rule(temperatura["Alta"] & humidade["Média"], potencia["Média"])
r9 = ctrl.Rule(temperatura["Alta"] & humidade["Alta"], potencia["Alta"])

regras = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
potencia_ctrl = ctrl.ControlSystem(regras)

potencia_sim = ctrl.ControlSystemSimulation(potencia_ctrl)

print("Teste 1: \nTemperatura: 20 \nHumidade: 30")
potencia_sim.input["Temperatura"] = 20
potencia_sim.input["Humidade"] = 30
potencia_sim.compute()
resp = potencia_sim.output["Potência"]
print("Potência:", resp)

print("\nTeste 2: \nTemperatura: 30 \nHumidade: 15")
potencia_sim.input["Temperatura"] = 30
potencia_sim.input["Humidade"] = 15
potencia_sim.compute()
resp = potencia_sim.output["Potência"]
print("Potência:", resp)

print("\nTeste 3: \nTemperatura: 35 \nHumidade: 30")
potencia_sim.input["Temperatura"] = 35
potencia_sim.input["Humidade"] = 30
potencia_sim.compute()
resp = potencia_sim.output["Potência"]
print("Potência:", resp)

print("\nTeste 4: \nTemperatura: 10 \nHumidade: 70")
potencia_sim.input["Temperatura"] = 10
potencia_sim.input["Humidade"] = 70
potencia_sim.compute()
resp = potencia_sim.output["Potência"]
print("Potência:", resp)
# pip install mip==1.4.2

from mip import *
resistores = []
resistores_qtd = []

index = 1
print("Digite os resistores a sua disposição:")
while (True):
    r = input(f"r{index}: ")
    if (r == ""):
        break
    qtd = int(input(f"Quantidade de r{index}: "))
    index += 1

    resistores.append(float(r))
    resistores_qtd.append(int(qtd))


objetivo = float(
    input("Digite qual a resitor equivalente você deseja obter: "))
# objetivo = 7.5

m = Model()

# Adiciona as variaveis
y = [m.add_var(name=f"r{i+1}", var_type=INTEGER, lb=0)
     for i in range(len(resistores))]

# Adiciona as condições
m += xsum((1/resistores[i])*y[i]*objetivo for i in range(len(resistores))) == 1
for r, qtd in zip(y, resistores_qtd):
    m += r <= qtd

# Adiciona a função objetiva
m.objective = xsum(y[i] for i in range(len(resistores)))

# Start algorithm1
m.max_gap = 0.05
status = m.optimize(max_seconds=300)
if status == OptimizationStatus.OPTIMAL:
    print('optimal solution cost {} found'.format(m.objective_value))
if status == OptimizationStatus.FEASIBLE:
    print('sol.cost {} found, best possible: {}'.format(
        m.objective_value, m.objective_bound))
if status == OptimizationStatus.NO_SOLUTION_FOUND:
    print('no feasible solution found, lower bound is: {}'.format(m.objective_bound))
if status == OptimizationStatus.OPTIMAL or status == OptimizationStatus.FEASIBLE:
    print('solution:')
    for v, r in zip(m.vars, resistores):
        print('{} : {} => {}'.format(v.name, v.x, r))

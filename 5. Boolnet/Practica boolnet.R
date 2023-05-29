install.packages('BoolNet') #instalar el paquete, solo se tiene que hacer una vez
library(BoolNet) # Llamarlo a nuestra sesión
data(cellcycle) # Cargar datos de prueba que vienen con la instalación del paquete
cellcycle
attractors <- getAttractors(cellcycle) # Calcular los atractores
par( mfrow=c(1,2) ) # hacer un espacio de 1 fila y 2 columnas en el área de plot
plotAttractors(attractors)
plotAttractors(attractors, mode="graph")

newnet <- fixGenes(cellcycle, "Rb", 0) # Esta es una deleción de Rb
newnet # es la nueva red con Rb deletado
getAttractors(newnet)
newnet2 <- fixGenes(newnet, 1, 1) # es una tercera red con Rb deletado y CycD sobreexpresado
getAttractors(newnet2)

### Crear tu propia red
sink('TestNet.bn') # crea un archivo de texto plano llamado 'TestNet.bn'
cat ("targets, factors\n")# en el primer renglón agrega el texto 'targets, factors' y luego un enter
cat("Gen1, Gen2 | !Gen3\n")# texto del segundo renglón
cat("Gen2, Gen3 & Gen4\n")# texto del tercer renglón
cat("Gen3, !Gen1\n") # texto del cuarto renglón
cat("Gen4, 1\n") # texto del quinto renglón
sink() # dejamos de escribir en el archivo de texto

MyNetwork <- loadNetwork("TestNet.bn") # cargar la red del archivo 'TestNet.bn'
MyNetwork
newAtt <- getAttractors(MyNetwork)
plotAttractors(newAtt)


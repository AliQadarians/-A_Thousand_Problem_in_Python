WeightOfOneMoleculeOfWater = 3.0 * 10**-23
weightOfOneMoleculeOfWater2 = 3.0e-23
WeightOfOneLiterOfWaterInTermsOfGrams = 980
weightOfWaterInLiters = int(input("Enter the weight of water in liters :    "))
numberOfWaterMolecules = (weightOfWaterInLiters * WeightOfOneLiterOfWaterInTermsOfGrams ) / WeightOfOneMoleculeOfWater 

print("Number of molecules in {} liters of water = {}".format(weightOfWaterInLiters,numberOfWaterMolecules))
# calculate upperbound for HP in 2D

# get protein string
# import global_vars
# global_vars.init()

# proteinstring = global_vars.protein_string
proteinstring = "HHPHHHPH"
protein_lenght = len(proteinstring)

even = 0
odd = 0
end_begin = 0
theoretical_optimum = 0

# count even and odd H's
for i in range(len(proteinstring) - 1):
	if i % 2 == 0:
		even += 1 
	else:
		odd += 1

# count beginning and end H's and C's
if proteinstring[0] == "H":
	end_begin += 1
elif proteinstring[protein_lenght - 1] == "H":
	end_begin += 1

# calculate theoretical max stability
if even < odd:
	theoretical_optimum = 2 * even + end_begin
else:
	theoretical_optimum = 2 * odd + end_begin

print("The (theoretical) optimum is: " + str(theoretical_optimum))
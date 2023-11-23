originalamount = 1000
rateofreturn = 7 / 100
year10 = 10
year20 = 20
year30 = 30


amountatyear10 = originalamount * ((1 +(7 / 100)) ** year10)
amountatyear20 = originalamount * ((1 +(7 / 100)) ** year20)
amountatyear30 = originalamount * ((1 +(7 / 100)) ** year30)

print(f"The amount on deposit at the end of ten years is ${amountatyear10:.3f}")
print(f"The amount on deposit at the end of twenty years is ${amountatyear20:.3f}")
print(f"The amount on deposit at the end of thirty years is ${amountatyear30:.3f}")

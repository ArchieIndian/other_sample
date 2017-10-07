# Finding all unique values from a feature when the feature itself is a comma separated field
# The name of the feature is assumed to be feature which may have values such as abc,def,ghi,jkl

# Here in the output, the unique features is printed. This shows all the values which have been value separated
# in any of the rows in that particular column 

all_named_features = data_target["named_feature"]
unique_features = {}
for val in all_named_features:
    try:
        vals = val.split(",")
        for v in vals:
            v = v.strip()
            try:
                unique_features[v] +=1
            except:
                unique_features[v] = 1
    except:
        pass
print unique_features


# Create dummy columns for every possible value

for key in unique_features.iterkeys():
    colname = 'prefix_'+str(key)
    data[colname] = data['unique_features'].str.contains(key)

# Populate the created columns on whether that key exists for that particular row 

d = {True:1, False:0}
def f(x):
    if x in d.keys():
        return d[x]
    else:
        return x
data = data.applymap(f)












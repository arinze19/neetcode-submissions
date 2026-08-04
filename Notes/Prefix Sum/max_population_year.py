def max_population_year(years):
    # can years be empty? No
    
    year = None
    max_size = 0
    
    for i in range(len(years)):
        start, end = years[i]
        count = 0
        for j in range(i, len(years)):
            next_start, next_end = years[j]
            # check if years overlap
            if next_start < end:
                count += 1
            
        if count > max_size:
            max_size = count 
            year = start
            
    return year


arr = [[1993,1999],[2000,2010]]
arr = [[1950,1961],[1960,1971],[1970,1981]]
print(max_population_year(arr))
            
            
            
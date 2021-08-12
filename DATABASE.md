# DATABASE

"""
Relationships

(1:N)
- Apartment - Photo (1 Apart -- has -> N Photo)
- Apartment - Flat (1 Apart -- has -> N Flat)
- City - Apartment (1 City -- has -> N Apartment)
- State - Apartment (1 State -- has -> N Apartment)
- Country - Apartment (1 Country -- has -> N Apartment)
- Neighborhood - Apartment (1 Neighborhood -- has -> N Apartment)
- Street - Apartment (1 Street -- has -> N Apartment)

(N:N)
* Apartment - Feature 
 - (1 Apart -- has -> N Feature)
 - (N Apart <- has -- 1 Feature)
 => (N:N - "ApartHasFeature")


* Apartment - Investment 
 - (1 Apart -- has -> N Investment)
 - (N Apart <- has -- 1 Investment)
 => (N:N - "ApartHasInvestment")
 
* Apartment - OutdoorSpace 
 - (1 Apart -- has -> N OutdoorSpace)
 - (N Apart <- has -- 1 OutdoorSpace)
 => (N:N - "ApartHasOutdoorSpace")

"""
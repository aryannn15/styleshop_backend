import pandas as pd

male = {

"slim": {
"date": [
{"top_color":"sky blue","top_type":"full sleeve shirt","bottom_color":"dark blue","bottom_type":"jeans"},
{"top_color":"white","top_type":"polo","bottom_color":"grey","bottom_type":"jeans"},
{"top_color":"sage green","top_type":"half sleeve shirt","bottom_color":"light blue","bottom_type":"jeans"}
],

"party": [
{"top_color":"black","top_type":"printed tee","bottom_color":"black","bottom_type":"jeans"},
{"top_color":"tie dye","top_type":"shirt","bottom_color":"grey","bottom_type":"jeans"},
{"top_color":"black","top_type":"striped shirt","bottom_color":"dark blue","bottom_type":"jeans"}
],

"casual": [
{"top_color":"black","top_type":"hoodie","bottom_color":"light blue","bottom_type":"jeans"},
{"top_color":"peach","top_type":"printed tee","bottom_color":"","bottom_type":"shorts"},
{"top_color":"sage green","top_type":"shirt","bottom_color":"grey","bottom_type":"jeans"}
],

"formal": [
{"top_color":"sky blue","top_type":"shirt","bottom_color":"beige","bottom_type":"formal pants"},
{"top_color":"white","top_type":"striped full sleeve","bottom_color":"navy","bottom_type":"formal pants"},
{"top_color":"black","top_type":"polo","bottom_color":"grey","bottom_type":"formal pants"}
]
},

# --------------------

"athletic": {
"date": [
{"top_color":"black","top_type":"polo","bottom_color":"grey","bottom_type":"jeans"},
{"top_color":"white","top_type":"polo","bottom_color":"dark blue","bottom_type":"jeans"},
{"top_color":"lilac","top_type":"polo","bottom_color":"light blue","bottom_type":"jeans"}
],

"party": [
{"top_color":"orange","top_type":"printed tee","bottom_color":"black","bottom_type":"jeans"},
{"top_color":"charcoal","top_type":"printed tee","bottom_color":"grey","bottom_type":"jeans"},
{"top_color":"navy","top_type":"printed tee","bottom_color":"dark blue","bottom_type":"jeans"}
],

"casual": [
{"top_color":"blue","top_type":"hoodie","bottom_color":"light","bottom_type":"jeans"},
{"top_color":"white","top_type":"printed tee","bottom_color":"","bottom_type":"shorts"},
{"top_color":"black","top_type":"hoodie","bottom_color":"","bottom_type":"cargo pants"}
],

"formal": [
{"top_color":"white","top_type":"full sleeve","bottom_color":"black","bottom_type":"formal pants"},
{"top_color":"sky blue","top_type":"shirt","bottom_color":"grey","bottom_type":"formal pants"},
{"top_color":"black","top_type":"polo","bottom_color":"navy","bottom_type":"formal pants"}
]
},

# --------------------

"muscular": {
"date": [
{"top_color":"black","top_type":"overshirt","bottom_color":"dark","bottom_type":"jeans"},
{"top_color":"white","top_type":"polo","bottom_color":"grey","bottom_type":"jeans"},
{"top_color":"red check","top_type":"overshirt","bottom_color":"black","bottom_type":"jeans"}
],

"party": [
{"top_color":"black","top_type":"tee","bottom_color":"","bottom_type":"cargo pants"},
{"top_color":"denim","top_type":"jacket","bottom_color":"black","bottom_type":"jeans"},
{"top_color":"ochre","top_type":"leather jacket","bottom_color":"dark","bottom_type":"jeans"}
],

"casual": [
{"top_color":"pine","top_type":"hoodie","bottom_color":"","bottom_type":"cargo pants"},
{"top_color":"graphic","top_type":"tee","bottom_color":"","bottom_type":"shorts"},
{"top_color":"black","top_type":"hoodie","bottom_color":"grey","bottom_type":"jeans"}
],

"formal": [
{"top_color":"white","top_type":"shirt","bottom_color":"navy","bottom_type":"formal pants"},
{"top_color":"sky blue","top_type":"shirt","bottom_color":"grey","bottom_type":"formal pants"},
{"top_color":"black","top_type":"polo","bottom_color":"black","bottom_type":"formal pants"}
]
},

# --------------------

"fat": {
"date": [
{"top_color":"lilac","top_type":"polo","bottom_color":"dark blue","bottom_type":"jeans"},
{"top_color":"black","top_type":"shirt","bottom_color":"grey","bottom_type":"jeans"},
{"top_color":"white","top_type":"polo","bottom_color":"black","bottom_type":"jeans"}
],

"party": [
{"top_color":"black","top_type":"hoodie","bottom_color":"dark","bottom_type":"jeans"},
{"top_color":"charcoal","top_type":"tee","bottom_color":"black","bottom_type":"jeans"},
{"top_color":"denim","top_type":"jacket","bottom_color":"black","bottom_type":"jeans"}
],

"casual": [
{"top_color":"black","top_type":"tee","bottom_color":"","bottom_type":"cargo pants"},
{"top_color":"dark","top_type":"hoodie","bottom_color":"","bottom_type":"jeans"},
{"top_color":"","top_type":"overshirt","bottom_color":"dark","bottom_type":"jeans"}
],

"formal": [
{"top_color":"black","top_type":"shirt","bottom_color":"black","bottom_type":"formal pants"},
{"top_color":"white","top_type":"shirt","bottom_color":"navy","bottom_type":"formal pants"},
{"top_color":"sky blue","top_type":"shirt","bottom_color":"grey","bottom_type":"formal pants"}
]
}

}


female = {

# =========================
"pear": {

"date": [
{"top_color":"yellow","top_type":"blouse","bottom_color":"dark blue","bottom_type":"jeans"},
{"top_color":"white","top_type":"halter neck top","bottom_color":"cream","bottom_type":"culottes"},
{"top_color":"pink","top_type":"flounced blouse","bottom_color":"cream","bottom_type":"palazzo"}
],

"party": [
{"top_color":"black","top_type":"strappy full length dress","bottom_color":"","bottom_type":""},
{"top_color":"blue floral","top_type":"strappy full length dress","bottom_color":"","bottom_type":""},
{"top_color":"silver","top_type":"halter neck sequined","bottom_color":"black","bottom_type":"wide leg leggings"}
],

"casual": [
{"top_color":"white","top_type":"printed tshirt","bottom_color":"cream","bottom_type":"cargo pants"},
{"top_color":"baby pink","top_type":"cardigan","bottom_color":"dark blue","bottom_type":"jeggings"},
{"top_color":"blue","top_type":"casual crop top","bottom_color":"white","bottom_type":"denim shorts"}
],

"formal": [
{"top_color":"caramel brown","top_type":"blazer","bottom_color":"black","bottom_type":"formal pants"},
{"top_color":"white","top_type":"buttoned full sleeve shirt","bottom_color":"white","bottom_type":"formal pants"},
{"top_color":"light blue","top_type":"full sleeve shirt","bottom_color":"khaki green","bottom_type":"formal pants"}
]
},

# =========================
"apple": {

"date": [
{"top_color":"yellow","top_type":"peplum top","bottom_color":"dark blue","bottom_type":"jeans"},
{"top_color":"red","top_type":"peplum top","bottom_color":"black","bottom_type":"trouser"},
{"top_color":"white","top_type":"shirt dress","bottom_color":"","bottom_type":""}
],

"party": [
{"top_color":"black","top_type":"mini dress","bottom_color":"","bottom_type":""},
{"top_color":"blue","top_type":"bodycon dress","bottom_color":"","bottom_type":""},
{"top_color":"brown","top_type":"bodycon full length dress","bottom_color":"","bottom_type":""}
],

"casual": [
{"top_color":"black","top_type":"printed tee","bottom_color":"cream","bottom_type":"cargo pants"},
{"top_color":"thulian pink","top_type":"hoodie","bottom_color":"dark blue","bottom_type":"jeggings"},
{"top_color":"red","top_type":"fine knit top","bottom_color":"black","bottom_type":"wide leg leggings"}
],

"formal": [
{"top_color":"caramel brown","top_type":"blazer","bottom_color":"white","bottom_type":"formal pants"},
{"top_color":"white","top_type":"buttoned full sleeve shirt","bottom_color":"black","bottom_type":"formal pants"},
{"top_color":"light blue","top_type":"full sleeve shirt","bottom_color":"khaki green","bottom_type":"formal pants"}
]
},

# =========================
"rectangle": {

"date": [
{"top_color":"chocolate brown","top_type":"crop top sleeveless","bottom_color":"cream","bottom_type":"palazzo"},
{"top_color":"beige","top_type":"tube top","bottom_color":"pink","bottom_type":"mini denim skirt"},
{"top_color":"red","top_type":"halter neck top","bottom_color":"dark blue","bottom_type":"jeans"}
],

"party": [
{"top_color":"black","top_type":"mini dress","bottom_color":"","bottom_type":""},
{"top_color":"white floral","top_type":"strappy full length dress","bottom_color":"","bottom_type":""},
{"top_color":"blue","top_type":"bodycon dress","bottom_color":"","bottom_type":""}
],

"casual": [
{"top_color":"pink","top_type":"tank top","bottom_color":"white","bottom_type":"denim shorts"},
{"top_color":"pastel yellow","top_type":"crop top","bottom_color":"dark blue","bottom_type":"jeggings"},
{"top_color":"white","top_type":"printed tshirt","bottom_color":"cream","bottom_type":"cargo pants"}
],

"formal": [
{"top_color":"light blue","top_type":"full sleeve shirt","bottom_color":"black","bottom_type":"formal pants"},
{"top_color":"caramel brown","top_type":"blazer","bottom_color":"white","bottom_type":"formal pants"},
{"top_color":"white","top_type":"buttoned full sleeve shirt","bottom_color":"khaki green","bottom_type":"formal pants"}
]
},

# =========================
"hourglass": {

"date": [
{"top_color":"brown","top_type":"off shoulder top","bottom_color":"dark blue","bottom_type":"jeans"},
{"top_color":"white","top_type":"halter neck top","bottom_color":"cream","bottom_type":"culottes"},
{"top_color":"pink","top_type":"flounced blouse","bottom_color":"pink","bottom_type":"mini denim skirt"}
],

"party": [
{"top_color":"blue","top_type":"bodycon dress","bottom_color":"","bottom_type":""},
{"top_color":"black","top_type":"mini dress","bottom_color":"","bottom_type":""},
{"top_color":"brown","top_type":"bodycon full length dress","bottom_color":"","bottom_type":""}
],

"casual": [
{"top_color":"thulian pink","top_type":"hoodie","bottom_color":"dark blue","bottom_type":"jeggings"},
{"top_color":"blue","top_type":"casual crop top","bottom_color":"white","bottom_type":"denim shorts"},
{"top_color":"white","top_type":"printed tshirt","bottom_color":"dark blue","bottom_type":"jeans"}
],

"formal": [
{"top_color":"caramel brown","top_type":"blazer","bottom_color":"black","bottom_type":"formal pants"},
{"top_color":"light blue","top_type":"full sleeve shirt","bottom_color":"white","bottom_type":"formal pants"},
{"top_color":"white","top_type":"buttoned full sleeve shirt","bottom_color":"khaki green","bottom_type":"formal pants"}
]
}

}


skin_tone_outfits = {

"porcelain": [
    "Navy ",
    "Sky blue ",
    "Lilac ",
    "Peach ",
    "Red ",
    "Silver "
],

"ivory": [
    "Sky blue",
    "Lilac",
    "Pink",
    "Baby pink",
    "Sage green",
    "Red"
],

"fair_beige": [
    "Peach",
    "Sage green",
    "Red",
    "Caramel brown",
    "Lilac",
    "Navy"
],

"beige": [
    "Navy",
    "Blue",
    "Lilac",
    "Red",
    "Chocolate brown",
    "Pink"
],

"warm_beige": [
    "Peach",
    "Orange",
    "Ochre",
    "Caramel brown",
    "Khaki green",
    "Peanut brown"
],

"dark_beige": [
    "Navy",
    "Cream",
    "Orange",
    "Red",
    "Pine green",
    "Caramel brown"
],

"natural": [
    "Blue",
    "Sky blue",
    "White",
    "Red",
    "Pink",
    "Sage green"
],

"honey": [
    "White",
    "Cream",
    "Blue",
    "Peach",
    "Red",
    "Chocolate brown"
],



"almond": [
    "White ",
    "Lilac ",
    "Sky blue",
    "Red",
    "Peanut brown",
    "Pink"
],


}

# Load once (important)
df = pd.read_excel("styleshop.xlsx")
print(df.columns)
df = df.fillna("")


df["color"] = df["color"].str.lower().str.strip()
df["category"] = df["category"].str.lower().str.strip()
df["gender"] = df["gender"].str.lower().str.strip()
df["occasion"] = df["occasion"].str.lower().str.strip()


def find_item(color, category, gender, occasion):
    color = color.lower().strip()

    match = df[
        (df["color"] == color) &
        (df["category"] == category) &
        (df["gender"] == gender) &
        (df["occasion"].str.contains(occasion))
    ]

    if len(match) > 0:
        return match.iloc[0].to_dict()

     
    # Fallback: ignore color, return any item for this category+gender+occasion

    fallback = df[

        (df["category"] == category) &

        (df["gender"] == gender) &

        (df["occasion"].str.contains(occasion, na=False))

    ]

    if len(fallback) > 0:

      return fallback.iloc[0].to_dict()

    return None  


def get_recommendations(user):

    body_dict = male if user["gender"] == "male" else female

    outfits = body_dict[user["body_shape"]][user["occasion"]]

    preferred_colors = [
        c.lower().strip()
        for c in skin_tone_outfits[user["skin_tone"]]
    ]

    scored_outfits = []

    for outfit in outfits:
        score = 2 if outfit["top_color"].lower() in preferred_colors else 0
        scored_outfits.append((score, outfit))

    scored_outfits.sort(reverse=True, key=lambda x: x[0])

    results = []

    for score, outfit in scored_outfits[:3]:

        top_item = find_item(
            outfit["top_color"],
            "top",
            user["gender"],
            user["occasion"]
        )

        bottom_item = find_item(
            outfit["bottom_color"],
            "bottom",
            user["gender"],
            user["occasion"]
        )

        results.append({
            "score": score,
            "top": top_item,
            "bottom": bottom_item
        })

    return results

# %%
import spacy

# %%
nlp = spacy.load("en_core_web_sm")

# %%
text = ("Anes Dzehverovic is a programmer who also studies physics and whishes to work at Google. ")

# %%
text

# %%
doc=nlp(text)

# %%
for token in doc:
    print(token)

# %%
for token in doc:
    if token.pos_=="NOUN":
        print(token)

# %%
for entity in doc.ents:
    print(entity.text, entity.label_)






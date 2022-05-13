from bs4 import BeautifulSoup
import requests
import re

from flask import Flask, render_template

html_page = requests.get("https://www.olx.ro/d/animale-de-companie/").text
soup = BeautifulSoup(html_page, "lxml")


class Dogs:

    number = 0
    babies = 0
    youngerThan1Year = 0
    olderThan1Year = 0
    sterilized = 0

    def __init__(
        self,
        breeds: dict = {},
        hairColor: dict = {},
        breedFilters: dict = {},
    ):
        self.breeds = breeds
        self.hairColor = hairColor
        self.breedFilters = breedFilters
        self.hairColorFilters = hairColorFilters


class Cats(Dogs):
    pass


class Parrot(Dogs):
    pass


class Fish(Dogs):
    pass


dogBreeds = {
    "Labrador": 0,
    "Golden Retriever": 0,
    "Bulldog": 0,
    "Bichon": 0,
    "Ciobanesc": 0,
    "Mops": 0,
    "Beagle": 0,
    "Husky": 0,
    "Others/Nespecificat": 0,
}
dogBreedFilters = {
    "Labrador": "la(m)?b[ar]*(a)?dor(i)?",
    "Golden Retriever": "(gold[aeă]n( )?)+|((r([ei]|ie)tr[iey]*?v[eăa]r(i)?)|reviver(i)?)+",
    "Bulldog": "b(l)?u(l+)?dog[si]|bul+[yi]",
    "Bichon": "b[ie][scș]h?on(i)?",
    "Ciobanesc": "ciob[aă]?ne[sș](c|ti)",
    "Mops": "mop[sș](i)?|p[ua]g[is]?",
    "Beagle": "b[ei](a)?g[eaă]?l[ei]?",
    "Husky": "h[ua]s(h)?k[iy]",
    "Others/Nespecificat": "c[aâ](i)?ne (maidanez[aă])?",
}

catBreeds = {
    "British shorthair": 0,
    "Scottish fold": 0,
    "Persana": 0,
    "Sphinx": 0,
    "Siameza": 0,
    "Birmaneza": 0,
    "Others/Nespecificat": 0,
}

catBreedsFilters = {
    "British shorthair": "british?[ |-]*shorthair|briti(s|ș) (s|ș)orthair|briti(s|ș) (s|ș)(h)?ortair|briti(s|ș) (s|ș)(h)?ort( |-)hair",
    "Scottish fold": "scot[t]?ish fold|scot[t]?i(s|ș) fold",
    "Persana": "persan(a|ă)",
    "Sphinx": "sphinx|sfinx",
    "Siameza": "siamez(a|ă)",
    "Birmaneza": "birmanez(a|ă)",
    "Others/Nespecificat": "(pisic[i]?[u]?[t|ț]?[a|ă]?)+( )?(maidanez[aă])?",
}

hairColor = {
    "Black": 0,
    "Alb": 0,
    "Gri": 0,
    "Maro": 0,
}

hairColorFilters = {
    "Black": "n[e](a)?gr[uaă]([tț][ăa])?|blac(k)?",
    "Alb": "alb(ă)?|white|galben|yellow",
    "Gri": "gr(i|[ea][yi])|sur",
    "Maro": "maro(n)?(iu)?|br[ao][uw]n",
}

parrotBreeds = {"Peruși": 0, "Others/Nespecificat": 0}

parrotBreedsFilters = {
    "Peruși": "peru(s|ș)i",
    "Others/Nespecificat": "papagal(i)?",
}

fishBreedsFilters = {
    "Discus": "dis(c)?us",
    "Koi": "(ck)oi",
    "Caras": "caras",
    "Others/Nespecificat": "pe(s|ș)t(i|e)([sș]or)?",
}
fishBreeds = {
    "Discus": 0,
    "Koi": 0,
    "Caras": 0,
    "Others/Nespecificat": 0,
}

otherFilters = {
    "Pui(orice)": 0,
    "Cu pedigree(orice)": 0,
    "Mancare": 0,
    "Obiecte pentru animale": 0,
}

dog = Dogs(dogBreeds, hairColor, dogBreedFilters)
cat = Cats(catBreeds, hairColor, catBreedsFilters)
parrot = Parrot(parrotBreeds, hairColor, parrotBreedsFilters)
fish = Fish(fishBreeds, {}, fishBreedsFilters)


html_page = requests.get("https://www.olx.ro/d/animale-de-companie/").text
soup = BeautifulSoup(html_page, "lxml")
# link_list = soup.find_all("a")
title_list = soup.find_all("h6", class_="css-v3vynn-Text eu5v0x0")
title_list = [x.text for x in title_list]


def searchForFilters(text):
    text = text.lower()
    foundAnimal = False
    # we search for food/animal related things
    if re.search(
        "dres[ae][jz]|tun[sd](ori)?|cuti[ei]*|cu(s|ș)c(a|ă)|a[cg]vari[iu]|botni(t|ț)(a|ă)|bol|zgard(a|ă)|ham|culcu(s|ș)|co(s|ș)|litier(a|ă)|coli[vb]([aă]|i[ie])|transport|zgard(aăe)|zgărzi+|tuns",
        text,
    ):
        otherFilters["Obiecte pentru animale"] += 1
        foundAnimal = True
    elif re.search("boabe|mancare(umeda)?|lapte|semin(t|ț)e|fulgi|hran(a|ă)", text):
        otherFilters["Mancare"] += 1
        foundAnimal = True

    if not foundAnimal:
        filtersChecker = {
            "filter1": False,
            "filter2": False,
            "filter3": False,
            "filter4": False,
            "filter5": False,
            "filter6": False,
            "filter7": False,
        }
        # testing if a dog breed is in the title
        for breedFilter in dog.breedFilters.keys():
            if re.search(dog.breedFilters[breedFilter], text):
                foundAnimal = True
                dog.breeds[breedFilter] += 1
                dog.number += 1
                dog.sterilized = 7
                filtersChecker["filter1"] = True

                # testing if a baby dog is in the title
                if re.search(
                    "c[aă][tț]e[la](u[sș]([aă])*)*|pui(u[tț]i)?([sș]or(i)*)?", text
                ):
                    foundAnimal = True
                    dog.babies += 1
                    otherFilters["Pui(orice)"] += 1
                    filtersChecker["filter2"] = True

                # testing if the dog is younger than a year
                if re.search("([1-9]|un)[1-9]?( )*an(i)?|1[2-9]( )*luni", text):
                    foundAnimal = True
                    dog.youngerThan1Year += 1
                    filtersChecker["filter3"] = True

                # testing if the dog is older than a year
                if not filtersChecker["filter3"] and re.search(
                    "([1-9]|un)[1-9]?( )*an(i)?|1[2-9]( )*luni", text
                ):
                    foundAnimal = True
                    dog.olderThan1Year += 1
                    filtersChecker["filter4"] = True

                # testing if the dog is sterilized
                if re.search("sterilizat[aă]?", text):
                    foundAnimal = True
                    dog.sterilized += 1
                    filtersChecker["filter5"] = True

                # testing if the dog got pedigree
                if re.search("pedigr(e*)(i)?e?", text):
                    foundAnimal = True
                    otherFilters["Cu pedigree(orice)"] += 1
                    filtersChecker["filter6"] = True
                # checking color of the dog
                for hairColor in hairColorFilters.keys():
                    if re.search(hairColorFilters[hairColor], text):
                        foundAnimal = True
                        dog.hairColor[hairColor] += 1
                        filtersChecker["filter7"] = True
                        break
                break

        # testing if the breed wasnt specified
        # testing if a baby dog is in the title
        if filtersChecker["filter1"] == False and re.search(
            "c[aă][tț]e[ila](u[sș]([aă])*)*", text
        ):
            foundAnimal = True
            dog.babies += 1
            dog.number += 1
            dog.youngerThan1Year += 1

        if re.search("pui(u[tț]i)?([sș]or(i)*)?", text):
            otherFilters["Pui(orice)"] += 1
            filtersChecker["filter2"] = True

    if not foundAnimal:
        filtersChecker = {
            "filter1": False,
            "filter2": False,
            "filter3": False,
            "filter4": False,
            "filter5": False,
            "filter6": False,
        }
        # testing if a cat breed is in the title
        for breedFilter in cat.breedFilters.keys():
            if re.search(cat.breedFilters[breedFilter], text):
                foundAnimal = True
                cat.breeds[breedFilter] += 1
                cat.number += 1
                filtersChecker["filter1"] = True

                # testing if a baby cat is in the title
                if re.search(
                    "pis(icu[tț][aăîâ]|oi)(a[sș]i?)?|pui(u[tț]i)?([sș]or(i)*)?", text
                ):
                    foundAnimal = True
                    cat.babies += 1
                    otherFilters["Pui(orice)"] += 1
                    filtersChecker["filter2"] = True
                    cat.sterilized = 5

                # testing if the cat is younger than a year
                if re.search("([1-9]|un)[1-9]?( )*an(i)?|1[2-9]( )*luni", text):
                    foundAnimal = True
                    cat.youngerThan1Year += 1
                    cat.olderThan1Year = 12
                    filtersChecker["filter3"] = True

                # testing if the cat is older than a year
                if not filtersChecker["filter3"] and re.search(
                    "([1-9]|un)[1-9]?( )*an(i)?|1[2-9]( )*luni", text
                ):
                    foundAnimal = True
                    cat.olderThan1Year += 1
                    cat.number += 1
                    filtersChecker["filter4"] = True

                # testing if the cat is sterilized
                if re.search("sterilizat[aă]?", text):
                    foundAnimal = True
                    cat.sterilized += 1
                    filtersChecker["filter5"] = True

                # testing if the cat got pedigree
                if re.search("pedigr(e*)(i)?e?", text):
                    foundAnimal = True
                    otherFilters["Cu pedigree(orice)"] += 1
                    filtersChecker["filter6"] = True
                for hairColor in hairColorFilters.keys():
                    if re.search(hairColorFilters[hairColor], text):
                        foundAnimal = True
                        cat.hairColor[hairColor] += 1
                        filtersChecker["filter7"] = True
                        break
                break

        # testing if the breed wasnt specified
        # testing if a baby cat is in the title
        if filtersChecker["filter1"] == False and re.search(
            "pis(oi(a[sș]i)?|ic([aă]|u(t|ț)(a|ă|e)))", text
        ):
            foundAnimal = True
            cat.babies += 1
            cat.number += 1
            cat.youngerThan1Year += 1

    if not foundAnimal:
        filtersChecker = {
            "filter1": False,
            "filter2": False,
            "filter3": False,
            "filter4": False,
            "filter5": False,
            "filter6": False,
        }
        for breedFilter in parrot.breedFilters.keys():
            if re.search(parrot.breedFilters[breedFilter], text):
                foundAnimal = True
                parrot.breeds[breedFilter] += 1
                parrot.number += 1
                filtersChecker["filter1"] = True
                for hairColor in hairColorFilters.keys():
                    if re.search(hairColorFilters[hairColor], text):
                        foundAnimal = True
                        parrot.hairColor[hairColor] += 1
                        filtersChecker["filter2"] = True
                        break
                break
        if filtersChecker["filter1"] == False and re.search(
            "papagal(i)*|peru[sș]i*", text
        ):
            foundAnimal = True
            parrot.number += 1

    if not foundAnimal:
        filtersChecker = {
            "filter1": False,
            "filter2": False,
            "filter3": False,
            "filter4": False,
            "filter5": False,
            "filter6": False,
        }
        for breedFilter in fish.breedFilters.keys():
            if re.search(fish.breedFilters[breedFilter], text):
                foundAnimal = True
                fish.breeds[breedFilter] += 1
                fish.number += 1
                filtersChecker["filter1"] = True
        if filtersChecker["filter1"] == False and re.search(
            "pe[sș]t[ei]([sș]or(i)*)?", text
        ):
            foundAnimal = True
            fish.number += 1


# # ITTERATE THROUGH PAGES
for i in range(2, 26):
    # Searching info in all the tiles of the current page
    for title in title_list:
        searchForFilters(title)

    next_page = "https://www.olx.ro/d/animale-de-companie/?page=" + str(i)
    html_page = requests.get(next_page).text
    soup = BeautifulSoup(html_page, "lxml")
    title_list = soup.find_all("h6", class_="css-v3vynn-Text eu5v0x0")
    title_list = [x.text for x in title_list]
    # print(f"Page {i}")
    # print(title_list)
    # print()
    # link_list = soup.find_all("a")


app = Flask(__name__)


@app.route("/")
def home():
    return render_template(
        "index.html",
        dogNumber=dog.number,
        dogBreeds=dog.breeds,
        dogColor=dog.hairColor,
        dogBabies=dog.babies,
        dogSmallerThanAYear=dog.youngerThan1Year,
        dogOlderThan1Year=dog.olderThan1Year,
        dogSterilized=dog.sterilized,
        catNumber=cat.number,
        catBreeds=cat.breeds,
        catColor=dog.hairColor,
        catBabies=cat.babies,
        catSmallerThanAYear=cat.youngerThan1Year,
        catOlderThan1Year=cat.olderThan1Year,
        catSterilized=cat.sterilized,
        parrotNumber=parrot.number,
        parrotBreeds=parrot.breeds,
        parrotColor=parrot.hairColor,
        fishNumber=fish.number,
        fishBreeds=fish.breeds,
        anyBaby=otherFilters["Pui(orice)"],
        PedigreeAnything=otherFilters["Cu pedigree(orice)"],
        animalFood=otherFilters["Mancare"],
        animalObjects=otherFilters["Obiecte pentru animale"],
    )


if __name__ == "__main__":
    app.run()

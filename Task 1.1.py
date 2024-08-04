import itertools


Kevin = {"Taylor Swift", "Kanye West", "Justin Beiber", "Travis Scott"}
Stuart = {"Justin Beiber", "Frank Ocean", "One Direction", "TheWeeknd"}
Bob = {"Justin Beiber", "Taylor Swift", "One Direction", "Joji"}
Edith = {"Joji", "Taylor Swift", "Frank Ocean", "Kanye West"}

DJs = {
    'Kevin' : Kevin,
    'Stuart' : Stuart,
    'Bob' : Bob,
    'Edith' : Edith
}


def pairs():
    djPairs = list(itertools.combinations(DJs.items(), 2))

    bestPairs = []

    for (dj1, artist1), (dj2, artist2) in djPairs:
        commonArtists = len(artist1.intersection(artist2))

        dj1_overlap = commonArtists/len(artist1) *100
        dj2_overlap = commonArtists/len(artist2) *100

        if dj1_overlap >= 30 and dj2_overlap >= 30 :
            bestPairs.append(((dj1,dj2), ((dj1_overlap+dj2_overlap)/2)))


    for bestPair in sorted(bestPairs, key = lambda bestPair: bestPair[1], reverse=True):
        print(f"{bestPair[0]}\t{bestPair[1]:.2f}\n")


if __name__=='__main__':
    pairs()
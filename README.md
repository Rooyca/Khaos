# Khaos

### [English](README.md) - [Spanish](/README(Spanish).md)

![Khaos-logo](LogoChaosFinal.png)

An API to generate randomness for (almost) everything

# What's Khaos?
Khaos (/ˈkeɪ.ɑs/) is the romanized form of "χάος" (Ancient Greek) and it's define as:

>  the mythological void state preceding the creation of the universe (the cosmos). [_Wikipedia_](https://en.wikipedia.org/wiki/Chaos_(cosmogony))

To me and many others chaos is one of the principal caractheristic of randomness because there is not posible prediction in it. I have been always facinated for the randomness itself, I found it extraordinarily beautiful. The fact that we can generate awesome things without understanding what's behind or, in other workds, "knowing" that there is nothing human behind it, that what has been made is just randomness, Khaos. That, folks, that's awesome.

Here we are going to have some fun trying to generate randomness (or pseudo-randomness) for (almost) everything... Let's get in to it!

# What does Khaos have to offer?

First of all, you can try Khaos here:

1. [RapidAPI](https://rapidapi.com/rooyca@gmail.com/api/random14/)
2. [Naked API](https://api.rooyca.xyz)

Or you can also run your own API by cloning this repository and running:

```bash
uvicorn main:app
```
Well, once you have choice the better option for you, let's see what we can do with this.

## Endpoints
There are ten endpoints and I'm going to divid them by sections:
- Security and privacy
- Information and data
- Words, games and general things.
 
### Security and privacy

![S&P](https://res.cloudinary.com/rooyca/image/upload/v1635035284/Images/S_P_yx1i6o.png)

We are all aware about the importance of having secure passwords. That they should be hard (or almost impossible) to crack, and even more at this time when our entire world depends on a string of numbers, words and symbols. One thing is for sure we should NOT let it to "luck"... or should we? As we said early, randomness its the absence of prediction so what better that generate passwords witch doesn't have any patron at all, making it impossible to humans to crack it. With machines its a little different because they are not like us... or not completely. So technically they COULD guess it, but chances are not that high. Although, be careful, this amply only if your "string" has at least twelve characters..

#### :small_red_triangle_down:Passwords

Query parameters:
|Parameter|Type|Default|Required|Description|
|---|---|---|---|---|
|leng|int|12|NO|Lenght of passwords|
|numb|int|1|NO|Number of passwords|
|include|str|"ULNS"|NO|Characters in passwords: (U)ppercases, (L)owercases, (N)umbers and (S)imbols

It's not a secret that technology has advance so much in the last years and it will keep advancing even more. That's why passwords are not (in some cases) the best options  for keeping us safe from loosing our money or personal data. Let me introduce you:

#### :small_red_triangle_down:Passphrases
What are they? In just a few works we could say that passphrases are more (or equally of) secure  than passwords but so much easy to remember. If you wanna know more about them read [this](https://www.techopedia.com/definition/4041/passphrase).

Query parameters:
|Parameter|Type|Default|Required|Description|
|---|---|---|---|---|
|n_words|int|7|NO|Word number of your passphrase|
|esp|bool|False|NO|Spanish passphrase|

##### :small_red_triangle_down:UUID

Here you can get a Universally Unique Identifier... nothing much. If you don't know what is that, you can check it out on [Wikipedia](https://en.wikipedia.org/wiki/Universally_unique_identifier)

### Information and data
![I&D](https://res.cloudinary.com/rooyca/image/upload/v1635035285/Images/I_D_pcljto.png)

There are some occasions where we want to register to one site but it just start to asking us a bunch of personal data that we are not willing to share. So these two endpoints are for those moments.

#### :small_red_triangle_down:Personal data

Here we will get:
- First name
- Last name
- Email address
- Phone number
- Country (Just USA at the moment)
- State
- Birthdate
- Gender

All this information is generate randomly but the phone number is base on the state, so its a little accurate (let me know if it's not :laughing:)

#### :small_red_triangle_down:CreditCard 
Here you can get a VALID random CC. ***It doesn't mean that it's a real CreaditCard***.
|Parameter|Type|Default|Required|Description|
|---|---|---|---|---|
|numb|int|1|NO|Number of CC's

### Words, games and general things
![GT](https://res.cloudinary.com/rooyca/image/upload/v1635035285/Images/G_efg3ph.png)

Last but not least here you will find a bunch of unrelated endpoints or, better said, about all type of things.
#### :small_red_triangle_down:Phrases
Have you ever had to write something but your brain just say: "No, no, no!"? Well, this may help you. At this endpoint you are going to generate random short phrases (just two words for now) that are grammatically correct and may (or may not) help you with your problem... And if it doesn't work at least you're going to have the chance to think in all type of bizarre things..
|Parameter|Type|Default|Required|Description|
|---|---|---|---|---|
|numb|int|1|NO|Number of phrasses|
|ussing|str|"AN"|NO|Phrases structure: Adjetive+Noun(AN), Noun+Noun(NN) or Verb+Noun(VN)|
#### :small_red_triangle_down:LoR Deck
Legends of Runeterra is a great cardgame (the best at the moment, in my opinion) but like all others card games it come to times where is just not much variety, everyone play the sames decks over and over. Well, you don't have to be like everyone else, in fact you could be the king of edgyness and play a compleatly random genered deck. Are you going to win? Probably not! Are you going to have fun? If you like to win then not, otherwise OF COURSE YOU WILL!

Just one thing, sometimes this generate invalid decks. When that happen you can make another request and try it again. (I'm already working on fix it)
#### :small_red_triangle_down:Colors
Now, let's imagine a scenario where you are working on something related with colors and you need to pick some colors. What do you do? If it's something really important you actually get into it and pick them but if it's something that doesn't need to be consistent or don't need to have relation between them you can checkout this endpoint and get a bunch of random colors.
|Parameter|Type|Default|Required|Description|
|---|---|---|---|---|
|numb|int|1|NO|Number of colors|
|using|str|hex|NO|Way of showing the colors: hex, rgb or all (All lowercases)|
#### :small_red_triangle_down:Choices
There is not much to say about this one... here you can make your choice without actually making a choice 😄.
This is broken at RappidAPI, if you really want to try it you can go to [Naked Endpoint](https://api.rooyca.xyz/v1/random/choice)
|Parameter|Type|Default|Required|Description|
|---|---|---|---|---|
|option|str|None|YES|The different options you have|
#### :small_red_triangle_down:Words
Do you want to make your vocabulary bigger? Or do you just need a random english word (for now. If you want to add your language please let me know) with meaning? Well this is your endpoint. 

I have a challenge for you... Do you think you can make three requests to this endpoint and get words you already know? It's pretty hard.
|Parameter|Type|Default|Required|Description|
|---|---|---|---|---|
|numb|int|1|NO|Number of words|

## TODO
- [ ] Generate random data from ambiental noice
- [ ] Generate random post-moderd piece of art
- [ ] Translate this to Spanish
- [ ] Your idea here...

## Colaborate

If you want to help me with ideas or anything else please contact me. (Contact info in my procfile)

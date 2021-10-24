# Khaos
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
Well, ones you have choice the better option tu you let's see what we can do with it.

## Endpoints
There are ten endpoints and I'm going to divid them by sections:
- Security and privacy
- Information and data
- Words, games and general things.
 
### Security and privacy

![S&P](https://res.cloudinary.com/rooyca/image/upload/v1635035284/Images/S_P_yx1i6o.png)

We are all aware about the importanse of have secure passwords that are preatty hard (or almost imposible) to crack. In this time when our entire world depends on a string of numbers, words and simbols we should not let it to destiny... or should we?
As we say early, randomness its the absense of prediction so what better thing that generate passwords that doesn't have any pathron at all, making it imposible to humans to crack it. With machines its a little different because they are not like us... or not compleatly. So technicly they COULD guess it, but chances are not that high.
Althoug this aply only if that string has at least twelve characteres.

#### :small_red_triangle_down:Passwords

Query parameters:
|Parameter|Type|Default|Required|Description|
|---|---|---|---|---|
|leng|int|12|NO|Lenght of passwords|
|numb|int|1|NO|Number of passwords|
|include|str|"ULNS"|NO|Characters in passwords: (U)ppercases, (L)owercases, (N)umbers and (S)imbols

It's not a secret that technology has advance so much in the last years and it will keep advancing even more in the coming years. That's why passwords are not the best options (in some cases) for keeping us safe from loosing our money or data. Let me introduce you to: 

#### :small_red_triangle_down:Passphrases
What are they? In just a few works we could say that passphrases are more secure and more easy to remeber than passwords. If you wanna know more about them. Read [this](https://www.techopedia.com/definition/4041/passphrase).

Query parameters:
|Parameter|Type|Default|Required|Description|
|---|---|---|---|---|
|n_words|int|7|NO|Word number of your passphrase|
|esp|bool|False|NO|Spanish passphrase|

##### :small_red_triangle_down:UUID

Here you can get a Universally Unique Identifier... nothing much. If you don't know what is that, you can check it out on [Wikipedia](https://en.wikipedia.org/wiki/Universally_unique_identifier)

### Information and data
![I&D](https://res.cloudinary.com/rooyca/image/upload/v1635035285/Images/I_D_pcljto.png)

There are some ocasions where we want to register to one site but it just start to asking us a bunch of personal data that we are not willing to share. So these two endpoints are for that moments.

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

All this information is generate randomly but the phonenumber is base on the state, so its a little accuarate (let me know if it's not :laughing:)

#### :small_red_triangle_down:CreditCard 
Here you can get a VALID random CC. ***It doesn't mean that it's a real CreaditCard***.
|Parameter|Type|Default|Required|Description|
|---|---|---|---|---|
|numb|int|1|NO|Number of CC's

### Words, games and general things

#### :small_red_triangle_down:Phrasses
#### :small_red_triangle_down:LoR Deck
#### :small_red_triangle_down:Colors
#### :small_red_triangle_down:Choices
#### :small_red_triangle_down:Words












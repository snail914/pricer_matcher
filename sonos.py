from stores import Stores, get_john_lewis_price, get_argos_price

urls = {
        Stores.John_Lewis: "https://www.johnlewis.com/sonos-beam-compact-smart-sound-bar-with-voice-control/black/p3585331",
        Stores.Argos: "https://www.argos.co.uk/product/8153368?clickSR=slp:term:sonos%20beam:2:18:1"
}

print(get_john_lewis_price(urls[Stores.John_Lewis]))
print(get_argos_price(urls[Stores.Argos]))

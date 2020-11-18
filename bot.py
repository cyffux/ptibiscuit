import discord
import os
import time
import random
from discord.ext.commands import Bot
from discord.ext import commands
bot = commands.Bot(command_prefix = "$")

@bot.event
async def on_ready():
    print("Bot is online and connected to Discord")

@bot.command()
async def biscuit(ctx):
    biscuit=["Demain, tu feras attention où tu mets tes pieds", "Yuki a très envie de toi","C'est une fille","tu es nul.le au lit","Tu te dois te soumettre à Allen","Tu te dois te soumettre à Arrix","Futur esclave tu es","Gigote le cul","Sale tiers état !","Tu seras Gigolo.Escort","tu seras riche","tu seras un manant à vie","You suck(s)","N’ignore pas les appels de ta mère ; elle va le savoir.","N’envoie pas de messages désespérés ivre à trois heures du matin.","Tu te feras draguer par Dilan","Tu te fera draguer par Yoshi","Tu resteras à jamais un charo","Charo ton.ta Voisin.e","Tes oncles reviendront te voler ta nourriture","Tu sauras réfléchir un jour","Réfléchis pas trop, ton cerveau risque de faire du pop-corn","Allen te fouetera et tu aimera","Lam mangera tes biscuits, cache-les","Tu es Beau.Belle","On te posera une cage.culotte de chasteté","tu trempes trop ton biscuit","ta peau servira à faire un sac","Bas les couilles, tu me soûles","Ton visage fondras","Tu parles trop fort","Continue de rêver, au moins tu dors","Grandis un peu","Tu sens le beurre de cacahuète, Lam te regarde étrangement","Tu es fort.e et indépendant.e","Tu joues au sims et ton chien se fait rôtir","Évite de jouer à la guitare, l'ombre de la mort n'est pas loin","Tu n'es pas seul.e, Engage un exorciste","Bien ! Tu as dépassé ta peur de te faire insulter, créature stupide","Ton rire fait saigner mes oreilles","Va dodoter","Va miamer","Va siester","Pense au BDSM, ça te fera peut être du bien","Ton niveau de nullité atteint celui de Yoshi"," Attention, Lam va te décolorer les cheveux"," Monstre mangeur de biscuit","Te rends-tu compte que tu m'as mangé pour avoir ce message","Tu dois faire des cookies à Chibi","Lombrique de bas étages"]
    choix=str(random.sample(biscuit,1))
    choix=choix.replace("[","")
    choix=choix.replace("]","")
    await ctx.send(str(choix))
    await ctx.send("🥠")
       
bot.run("Nzc4MzIxNzYyMDQ3MjMwMDIz.X7QSoA.K_IaFr8fsXq-VFpZSv_9NUF2Vi4")

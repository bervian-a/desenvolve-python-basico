import pip
import emoji


#entrada
print ("Emojis disponiveis:\n"
"😴 - :slepping_face:\n"
"❤️ - :red_heart:\n"
"👍 - :thumbs_up:\n"
"🤔 - :thinking_face:\n"
"🥳 - :partying_face:\n"
"🤩 - :star_struck:")

emojizar = (input("Digite uma frase e ela será emojizada: "))

print (f"Frase demojizada: \n{emojizar}")
print (f"Frase emojizada: \n{emoji.emojize (emojizar, language='alias', variant=emoji)}")

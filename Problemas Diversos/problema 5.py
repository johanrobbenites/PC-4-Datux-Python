from modulo import datos
import re
path = './src/re/short_tweets.csv'
analisis_sentimientos = datos.read_pandas(path,780,782)
regex = r"^[aeiouAEIOU]{2,3}\w*.txt"  # complete aqui
for tweet in analisis_sentimientos:
    print(tweet)
    
    # Encuentre todos los casos
    print(re.findall(regex, tweet))
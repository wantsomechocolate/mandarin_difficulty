import math, csv
import numpy as np
fp = r"global_wordfreq_release_UTF-8.txt"
#fh = open(fp)
#fh.close()
seen = {}
max_freq = 0
min_freq = float('inf')
all_freq = []
all_logs = []
with open(fp, encoding = 'utf-8') as fh:

	for line in fh.readlines():
		try:
			chars, freq = line.split()
			max_freq = max(max_freq,int(freq))
			min_freq = min(min_freq,int(freq))
			all_freq.append(int(freq))
			all_logs.append(math.log(int(freq)))
			for char in chars:
				if char in seen:
					seen[char]+=int(freq)
				else:
					seen[char]=int(freq)

		except ValueError:
			pass
			#print(line)


hist, bins = np.histogram(all_logs)

phrase_fp = r"sample_sentences.txt"
with open(phrase_fp, encoding='utf-8') as phrase_fh:
	phrases = phrase_fh.readlines()[1:]


#phrases = [
#	'我是一个红色的苹果',
	#'如果你杀了我，你也不能从这儿活着走出去',
	#'谁都有自己的利益，我也是',
	#'天诛地灭',
	#'这个句子没有那么复杂',
	#'科学考前复习 B 组作答技巧 6 （二） 目的  在进行实验前，我们必须知道进行实验的目的，才能明确知道该如何进行实验，并获取实验结果。 1. 先找出实验中必须改变的事项和必须观察/测量的事项。 2. 有两种作答方式： i. 为了研究/探讨（必须改变的事项）和（必须观察/测量的事项）之间的关系。 ii. 为了研究/探讨（必须改变的事项）如何影响（必须观察/测量的事项）。 *用方法ii 时，必须先填写“必须改变的事项”，不可颠倒。因此，考生最好使用方法i。',
	#'科学考前复习组作答技巧目的在进行实验前我们必须知道进行实验的目的才能明确知道该如何进行实验并获取实验结果先找出实验中必须改变的事项和必须观察测量的事项有两种作答方式为了研究探讨必须改变的事项和必须观察测量的事项之间的关系为了研究探讨必须改变的事项如何影响必须观察测量的事项用方法时必须先填写必须改变的事项不可颠倒因此考生最好使用方法',
	#'中美关系日益严峻，作为国际性的人才，我们能为社会做些什么',
	#'怀胎十月',
	#'这一天，妈妈把小山羊叫到面前说：“爸爸、妈妈年龄大了不能经常去看你的外婆家了，你大了，应该替爸妈去看望你的外婆去了！要不认识路的话，路上要有礼貌向别人问路。”小山羊说。',
	#'这一天妈妈把小山羊叫到面前说爸爸妈妈年龄大了不能经常去看你的外婆家了你大了应该替爸妈去看望你的外婆去了要不认识路的话路上要有礼貌向别人问路小山羊说',

#	'看你的刀快还是我的抢快。',
#	'当然十你的枪快，不过今天我来这儿并不是为了逮捕你',
#	'算你聪明，你早往前版半步，我会打爆你的脑袋',
#	'如果你杀了我你也不能从这活着走出去',
#	'你就鱼死网破',
#	'我的队友们五分钟以后会冲进来，留给我们的时间不多了',
#	'你是指。。。',
#	'跟我合作，黄金分我一半儿',
#	'你真是狮子大张口啊，为了这个案子我整整策划了两年',
#	'人不为己天诛地灭，谁都有自己的利益我也是。',
#       '
#]

with open('output.csv', 'w', encoding='utf-8', newline='') as csvfile:
	csv_writer = csv.writer(csvfile,delimiter=' ')

	for line in phrases:
		phrase = line.split()[0]
		phrase_set = set(phrase)
		#phrase = '我是一个红色的苹果'
		l = len(phrase_set)
		sum_of_freq=0
		sum_of_logs=0
		phrase_logs = []
		for char in phrase_set:
			if char in seen:
				phrase_logs.append(math.log(seen[char]))
				freq = seen[char]
				log = math.log(freq)
				#print(char,freq,log)
				sum_of_freq+=freq 
				sum_of_logs+=log 
			else:
				#pass
				l-=1
				#print(char,"was not in seen")

		score_2_offset = 19
		score_2_multiplier = 2
		score_2_min = 0
		score_2_max = 10

		phrase_hist, phrase_bins = np.histogram(phrase_logs,bins)
		score_1 = sum([phrase_hist[-i]*(i) for i in range(1,len(phrase_hist)+1)])/sum(phrase_hist)	
		score_2 = min(score_2_max,max(score_2_min,((score_2_offset-(sum_of_logs/l))*score_2_multiplier)))
		#print(phrase,",",score_1,",",score_2)
		csv_writer.writerow([phrase,score_2])
		#print("the log of the average is", math.log(sum_of_freq/l))
		#print("the average of the logs is", sum_of_logs/l)
		#print("")
#print(max_freq, math.log(max_freq)) #max is 2002074595 and ln of that is 21.42
#min score was like 25 or something like that which sounds familiar, ln of that is 3.21



## Definitely seems like average of the logs is better


# I think this may only works for shorter sentences, or sentences of the same length because if a long sentence has many easy words and
# then one extremely difficult word, then this won't really capture that. So maybe I need to take some sort of bucketing approach
# and then I can look at the distribution of difficult words and use that distribution somehow, like flatten each group no matter how many words
# there are in that group? 
# Or maybe at that point I could do something like characters/sentence



# Maybe including known words is central to this whole endeavor. 
# It helps with segmentation
# it helps determine the "grade of something"
# like if I have a list of words I already know and I remove them before calculating the "difficulty" of a sentence or text based on 
# only words I don't know, it would be more personalized and accurate. 
# because some of these sentences get low scorew just because they have repitition of very common words
# ANOTHER THING I SHOULD BE DOING IS EXCLUDING DUPLICATES, at least until I start removing known words,
# but really, does having the same uncommon word in a sentence actually make it harder? I would guess maybe marginally? 
# but also maybe not at all. You have to look that word up anyway 

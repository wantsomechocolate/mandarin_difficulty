Trying to gauge difficulty based on character frequency only.
number of characters that are similar looking to that character? hahaha should probably only have a small impact
But how do I get frequencies for only chinese characters? I guess I could go through the official list of characters, and then get their total freqencies across all words. 
So say I have this frequency information, do I use a logarithmic scale? is my scale 11-20?

我是一个红色的苹果 

wo, shi, yi, ge, de, are all extremely common
hong, se, guo, are probably next most common
maybe ping is slightly less common/frequent then the rest. 
So how to grade this sentence? the average frequency? 
It would be nice to get the actually frequency data first to play around with it. 



How would an API for this look

the request needs to have:

mainendpoint
text
delimiter
method?
version
language I guess in case I ever wanted to do other languages?

difficultyestimater.com/v1?text=asdf#....

And the response will be json probably
{status..

data:[{text:"asdf",difficulty:8},....]

request_string?:

}





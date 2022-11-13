class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = [] # Collections used to get all the lines.
        
        i = 0 # Index of the current word
        current_width = 0 # Keeps track of the current width we've processed for a given line.
        line = []
        
        while i < len(words):
            word = words[i]
            
			# Verify that the current_width + current word does not exceed the max width.
            if (current_width + len(word)) <= maxWidth:
                line.append(word)
                current_width += len(word) + 1 # Since all words must have a minimum of 1 space, that +1 is for the space
                i += 1
            else: 
				# We've reached the point where we can't process any new words. So we process the line seen so far.
				# Note: We don't increment i here because we want to reprocess it for the next line.
                current_line = ""
				
				# Calculate the total number of spaces we need. In the if statement above, we added +1 for space between words.
				# Here we're removing all those for easier calculation in the future. That is what the + len(line) is for; 1 space per word.
                necessary_spaces = maxWidth - current_width + len(line) 
                if len(line) == 1: # Edge case where the line only has 1 word.
                    current_line += line[0] + " " * necessary_spaces # Append all spaces at the end in this instance.
                else: # There's more than 1 word in the line so we need to process all of them.
                    
                    for j in range(len(line)):
                        line_word = line[j]
						# So between each word we need to distribute spaces evenly. 
						# The intuition here is that, except for the last word, we'll need to calculate how many spaces we need.
						# Example: if you have these words for a line ["This", "is", "an"] with a maxWidth = 16
						# there are 3 words and you need to divide it between 2 spaces: "this" and "is" and "is" and "an" so that means
						# you need 8 spaces evenly. We use remaining_words below to calculate the required_spaces below using the logic seen below.
						# For the last word in a line, we don't need any spaces so it is always 0.
						# We use the ceil function here because if maxWidth is odd, then we have to distribute to the left side first (or greedily).
                        remaining_words = len(line) - (j + 1)
                        required_spaces = ceil(necessary_spaces / remaining_words) if remaining_words else 0
                        current_line += line_word + " " * required_spaces
                        necessary_spaces -= required_spaces # Subtract from necessary spaces. In the example above it would take 8 -> 4.
						
                lines.append(current_line) # Add the result of the current line.
                line = []
                current_width = 0

		# It's possible that we have processed all the words, but have some left over in the line. So we'll add the remainder.
		# Based on the problem description we want to only add a space between each word here and then add any remaining
		# spaces at the end.
        if line: 
            necessary_spaces = maxWidth - current_width + 1
            current_line = ' '.join(line) + " " * necessary_spaces
            lines.append(current_line)
        return lines
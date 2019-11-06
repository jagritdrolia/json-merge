# json-merge
Merge 2 or more json files into single output json using python 

Input form 

* Enter the folder path of your file: /Users/jagrit.drolia/Desktop/
* Enter the prefix of your file: test
* Enter the prefix of your output file: result
* Enter the max file size in bytes: 1022

* Algorithmic Complexity of algorithm 

	It is merging the file in O(N * no_of_files). 
	I am scanning each file once and store the key and value. 
	If in next file I am getting the same key I am appending that key to the same key.

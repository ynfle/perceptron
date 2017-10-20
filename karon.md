```java
	public SortedSet<String> wordsStartingWith(String prefix) {
		SortedSet<String> returnList = new TreeSet<String>();
		int length = prefix.length();
		prefix = prefix.toLowerCase();
		String endWord = prefix.substring(0, length - 1) + (char) (prefix.charAt(length - 1) + 1);
		boolean[] truthArray = { this.lookUp(prefix), this.lookUp(endWord) };
		words.add(prefix);
		words.add(endWord);
		this.wordList = new ArrayList<String>(words);

		if (truthArray[0]) {
			returnList.addAll(wordList.subList(wordList.indexOf(prefix), wordList.indexOf(endWord)));
		} else {
			returnList.addAll(wordList.subList(wordList.indexOf(prefix) + 1, wordList.indexOf(endWord)));
		}
		if (truthArray[1]) {
			words.remove(endWord);
		}
		wordList = new ArrayList<>(words);
		return returnList;
	}
```
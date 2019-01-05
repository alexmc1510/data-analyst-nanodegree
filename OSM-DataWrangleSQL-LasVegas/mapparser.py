{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'bounds': 1,\n",
      " 'member': 4657,\n",
      " 'nd': 1367246,\n",
      " 'node': 1153019,\n",
      " 'osm': 1,\n",
      " 'relation': 573,\n",
      " 'tag': 512985,\n",
      " 'way': 125179}\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "Your task is to use the iterative parsing to process the map file and\n",
    "find out not only what tags are there, but also how many, to get the\n",
    "feeling on how much of which data you can expect to have in the map.\n",
    "Fill out the count_tags function. It should return a dictionary with the \n",
    "tag name as the key and number of times this tag can be encountered in \n",
    "the map as value.\n",
    "Note that your code will be tested with a different data file than the 'example.osm'\n",
    "\"\"\"\n",
    "import xml.etree.cElementTree as ET\n",
    "import pprint\n",
    "\n",
    "def count_tags(filename):\n",
    "    tags = {}\n",
    "    for event, elem in ET.iterparse(filename): #iterable that returns a stream of (event, element) tuples\n",
    "        tag = elem.tag\n",
    "        tags[tag] = tags.get(tag, 0) + 1\n",
    "        \n",
    "    return tags\n",
    "\n",
    "\n",
    "\n",
    "tags = count_tags('data/las-vegas.osm')\n",
    "pprint.pprint(tags)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:DAND]",
   "language": "python",
   "name": "conda-env-DAND-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 20 5\n",
      " ? 1 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " ! 3 4 5\n",
      " ? 1 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " ! 1 4 15\n",
      " ? 1 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "def primeFactors(n):\n",
    "    t=[]\n",
    "    if n%2==0:\n",
    "        t.append(2)\n",
    "    while n % 2 == 0: \n",
    "        n = n / 2\n",
    "    for i in range(3,int(math.sqrt(n))+1,2):\n",
    "        if n%i==0:\n",
    "            t.append(i)\n",
    "        while n % i== 0: \n",
    "            n = n / i \n",
    "    if n > 2: \n",
    "        t.append(int(n))\n",
    "    return t\n",
    "k,q=map(int,input().split())\n",
    "p=primeFactors(k)\n",
    "x=[0]*100000\n",
    "\n",
    "while q>0:\n",
    "    q-=1 \n",
    "    a=list(input().split())\n",
    "    l=int(a[1])\n",
    "    r=int(a[2])\n",
    "    if a[0]=='!':\n",
    "        k=int(a[3])\n",
    "        for i in range (l,r+1):\n",
    "            if x[i]==0:\n",
    "                x[i]=k \n",
    "    else:\n",
    "        ans=0\n",
    "        for i in p:\n",
    "            for j in range(l,r+1):\n",
    "                if x[j]==0:\n",
    "                    continue\n",
    "                if x[j]%i==0:\n",
    "                    ans+=1 \n",
    "                    break\n",
    "        print(ans)\n"
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
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

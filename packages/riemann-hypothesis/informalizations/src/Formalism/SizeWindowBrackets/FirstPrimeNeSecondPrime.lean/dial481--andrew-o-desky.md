---
{
  "module": "src/Formalism/SizeWindowBrackets/FirstPrimeNeSecondPrime.lean",
  "declarations": [
    "Formalism.LFunctionChainParameters.characterSumData.ASK",
    "Formalism.LFunctionChainParameters.characterSumData.ArithData",
    "Formalism.LFunctionChainParameters.characterSumData.IsInert",
    "Formalism.LFunctionChainParameters.characterSumData.MAIN",
    "Formalism.LFunctionChainParameters.characterSumData.askD",
    "Formalism.LFunctionChainParameters.characterSumData.askP",
    "Formalism.LFunctionChainParameters.characterSumData.chC",
    "Formalism.LFunctionChainParameters.characterSumData.partner"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Weighted prime-power count and its main term

[Definition / hypothesis ANT.D068](https://andrewodesky.com/rh/lean/Formalism.LFunctionChainParameters.characterSumData.ASK/)

**The group.** Let $H$ be a finite abelian group of order $n$, written additively, and put $$G=(\mathbb Z/2\mathbb Z)^2\times H,\qquad\Phi=\{((0,\beta),h):\beta\in\mathbb Z/2\mathbb Z,\ h\in H\},\qquad f=|\Phi|=2n.$$ Let $\widehat G=\operatorname{Hom}(G,\mathbb C^\times)$ be the group of characters of $G$, and let $\chi_C\in\widehat G$ be the character with kernel $\Phi$: $$\chi_C((\alpha,\beta),h)=\begin{cases}1,&\alpha=0,\\-1,&\alpha=1.\end{cases}$$ For $t\in H$, define the map $P_t:G\to G$ by $$P_t(\sigma)=c+\sigma+((0,0),t),\qquad c=((1,1),0).$$ It maps the complement $G\setminus\Phi$ bijectively onto $\Phi$.

**The data.** Let $N,q,d\ge0$ be integers. For every integer $p\ge0$, let $I_p$ be a subgroup of $G$ and $F_p$ an element of $G$. Let $\kappa:\widehat G\to\mathbb C$ be a function.

**The count.** For an integer $i\ge1$, write $iF_p$ for the sum of $i$ copies of $F_p$, and for a real number $y$ write $(y)_+=\max(y,0)$. For a real number $s$, an element $t\in H$ and a function $\omega:G\to\mathbb R$, the weighted prime-power count is $$A(s,t,\omega)=2\sum_{p}\log p\sum_{\substack{1\le i\le N\\iF_p\notin\Phi}}\bigl(s/p^i-\omega(P_t(iF_p))\bigr)_+ +\log d\sum_{i=1}^N\sum_{\substack{\sigma\in G\setminus\Phi\\\sigma-iF_d\in I_d}}\bigl(s/d^i-\omega(P_t(\sigma))\bigr)_+,$$ where $p$ runs over the primes $p\le N$ such that $p\notin\{2,q,d\}$ and $F_p\notin\Phi$. Every argument of $\omega$ in this formula lies in $\Phi$.

**The main term.** Let $\gamma$ be Euler's constant. For a real number $s\ge0$ and a function $\omega:G\to\mathbb R$ that is positive on $\Phi$, the main term of the count is the complex number $$M(s,\omega)=s\Bigl(\log s-1-\gamma+\kappa(\chi_C)-\frac1f\sum_{\rho\in\Phi}\log\omega(\rho)\Bigr).$$

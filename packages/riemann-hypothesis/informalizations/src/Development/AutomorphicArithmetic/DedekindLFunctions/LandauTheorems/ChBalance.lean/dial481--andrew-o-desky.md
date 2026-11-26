---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChBalance.lean",
  "declarations": [
    "Deduction.ch_balance"
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

## Prime-power Fourier identity

[Theorem ANT.0114](https://andrewodesky.com/rh/lean/Deduction.ch_balance/)

We express a weighted sum over prime powers, with an explicit correction term, in terms of smoothed character sums.

Let $H$ be a finite abelian group, written additively, and put $G=(\mathbb Z/2\mathbb Z)^2\times H$. Let $\widehat G$ be its group of complex characters, that is, homomorphisms $\chi:G\to\mathbb C^\times$. Write $1$ for the trivial character and $\overline z$ for complex conjugation. For $g=((\alpha,\beta),h)\in G$, define the subgroup $\Phi$ and character $\chi_C$ by $$\Phi=\{((0,\beta),h):\beta\in\mathbb Z/2\mathbb Z,\ h\in H\},\qquad \chi_C(g)=\begin{cases}1,&\alpha=0,\\-1,&\alpha=1.\end{cases}$$ Put $f=|\Phi|=2|H|$, $c=((1,1),0)$ and $s_0=((1,0),0)$. For $t\in H$, define the translation $P_t:G\to G$ by $$P_t(g)=c+g+((0,0),t).$$

Let $\mathbb N=\{0,1,2,\ldots\}$. Choose $q,d\in\mathbb N$, a finite set $S\subset\mathbb N$, and, for each $p\in\mathbb N$, a subgroup $I_p\le G$ and an element $F_p\in G$. Assume:

1. $d$ is prime, $2,q\in S$, and $d\notin S$.
2. $I_p=\{0\}$ for every prime $p\notin S\cup\{d\}$.
3. $I_p\subset\Phi$ and $F_p\in\Phi$ for every $p\in S$.
4. $I_d=\{0,s_0\}$.

For a positive integer $n$ and a prime $p$, let $v_p(n)$ be the exponent of $p$ in $n$. For $i\in\mathbb N$ and $u\in G$, write $iu$ for the sum of $i$ copies of $u$. For $\chi\in\widehat G$ and $n\ge1$, define $$a_\chi(n)=\prod_{\substack{p\mid n\\p\ \mathrm{prime}}}\frac1{|I_p|}\sum_{z\in I_p}\chi(v_p(n)F_p+z),$$ where an empty product is $1$. Let $\Lambda$ be the von Mangoldt function: $\Lambda(p^i)=\log p$ for primes $p$ and integers $i\ge1$, and $\Lambda(n)=0$ for positive integers that are not prime powers. All logarithms are natural. Let $\gamma$ be Euler's constant. Given any function $\kappa:\widehat G\to\mathbb C$, define the smoothed character sums, for $y>0$, by $$g_\chi(y)=\begin{cases}\displaystyle\sum_{1\le n\le y}\Lambda(n)(y/n-1)-y\log y+(1+\gamma)y,&\chi=1,\\[2pt]\displaystyle\sum_{1\le n\le y}\Lambda(n)a_\chi(n)(y/n-1)+y\kappa(\chi),&\chi\ne1,\end{cases}$$ where each sum over $n$ runs over positive integers.

Fix a real number $a>0$, $t\in H$ and $w:G\to\mathbb R$ such that $w(\rho)>0$ for every $\rho\in\Phi$. Choose $N\in\mathbb N$ satisfying $a/w(\rho)\le N$ for every $\rho\in\Phi$. For $g\notin\Phi$, put $W_g=w(P_t(g))$; this is positive because $P_t(g)\in\Phi$. For real $x$, write $(x)_+=\max(x,0)$. Define $$\begin{aligned} A={}&2\!\sum_{\substack{p\le N\ \mathrm{prime},\ p\notin\{2,q,d\}\\F_p\notin\Phi}}\!\log p\sum_{\substack{1\le i\le N\\iF_p\notin\Phi}}(a/p^i-W_{iF_p})_+\\ &+\log d\sum_{i=1}^N\sum_{\substack{g\in G\setminus\Phi\\g-iF_d\in I_d}}(a/d^i-W_g)_+,\\[2pt] M={}&a\left(\log a-1-\gamma+\kappa(\chi_C)-\frac1f\sum_{\rho\in\Phi}\log w(\rho)\right). \end{aligned}$$ Here $p,i$ are natural numbers. Then $$A-M=\frac1f\sum_{g\in G\setminus\Phi}\sum_{\chi\in\widehat G}\overline{\chi(g)}\,W_g\,g_\chi(a/W_g)$$ as an identity in $\mathbb C$.

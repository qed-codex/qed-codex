---
{
  "module": "src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChCore.lean",
  "declarations": [
    "Deduction.ch_core"
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

## From uniform prime counts to a character sum

[Theorem ANT.0158](https://andrewodesky.com/rh/lean/Deduction.ch_core/)

Fix real numbers $C\ge0$, $\varepsilon>0$, $C_a,K_0,c,M$ with $|c|\le1$. There exists $x_1\in\mathbb R$, depending only on these fixed numbers, with the following property for every $x\ge x_1$ and every choice of the data below.

Let $H$ be a finite abelian group of order $n$, let $H_0\le H$, and let $T,T_2\subset H$ with $T_2\subset H_0$. Use $G,\Phi,c_0=((1,1),0),s_0=((1,0),0)$, inertia groups, Frobenius elements and the functions $g_\gamma,A,M_0$ of ([Prime-power Fourier identity](https://andrewodesky.com/rh/lean/Deduction.ch_balance/)), writing $c_0$ for that identity's element $c$ and $M_0$ for its main term. Assume every arithmetic hypothesis of that identity, for a finite set $S$ containing $2,q$ and excluding the prime $d$. The function $\kappa:\widehat G\to\mathbb C$ is arbitrary.

Choose $m,N\in\mathbb N$, $a:H\to\mathbb R$, and $w:H\times\{0,\ldots,m-1\}\times G\to\mathbb R$; write $a_t=a(t)$ and $w_{u,j}(\rho)=w(u,j,\rho)$. Choose real numbers $b,b',k,a_0,\eta,X',\theta$ with $b,k,b',X'>0$ and $a_0,\eta,\theta\ge0$. Require $b'X'\le xb$, $|a_t/b-x|\le1$ for $t\in T$, and the following conditions for all $u\in H_0$ and $0\le j<m$:

The weights are positive on $\Phi$. On $$\{((0,1),s+u):s\in T_2\}$$ they lie in $[b,b+\eta+1]$; on the remainder of $\Phi$ they are at most $2b'$. Also $a_t/w_{u,j}(\rho)\le N$ for $t\in T$ and $\rho\in\Phi$.

Require, for every $\gamma\in\widehat G$ and $y\ge X'/3$, $$|g_\gamma(y)|\le y\theta,$$ and require $$2(2n)(x+1)\theta\le1/x,\qquad6(2n)(x+1)(\eta+1)\le b/x.$$ The numerical size conditions are $$a_0\le2xb,\quad |T|\ge\tfrac12nx^{-\varepsilon/8},\quad |T_2|/n\ge x^{-\varepsilon},$$ $$x^{1/2-\varepsilon}\le m\le x^{1/2+\varepsilon/2},\qquad xm\le k\le n^2x^{1/2-\varepsilon}.$$

Let $\Psi_0$ be the characters of $G$ trivial on $\{0\}\times H_0$, and choose $K\subset\Psi_0$ containing the trivial character. Assume $\gamma(s_0)=1$ for $\gamma\in K$, $|\Psi_0|\le M$, and, for each $\gamma\in K$ nontrivial on $\{0\}\times H$, $$\left|\sum_{t\in T}\gamma(0,t)-c|T|\right|\le Mx^{-1+\varepsilon}|T|.$$ Assume $|\kappa(\gamma)|\le K_0$ for every nontrivial $\gamma\in K$, and $|\kappa(\gamma)|\le C_a\log x$ for every $\gamma\in\Psi_0\setminus K$.

Set $$B=|T|a_0(1+m^2/k)+m\left(2nmbx^\varepsilon+\frac{|T_2|kbx^\varepsilon}{n(nx^{-\varepsilon})}\right).$$ Finally, suppose that for every $u\in H_0$, $$\sum_{t\in T}\sum_{j=0}^{m-1}\{A(a_t,t,w_{u,j})-\Re M_0(a_t,w_{u,j})\}\le x^{C\varepsilon}B.$$ Define $d_\gamma=1$ if $\gamma$ is trivial on $\{0\}\times H$, and $d_\gamma=c$ otherwise. Then $$\sum_{\gamma\in K}d_\gamma\Re g_\gamma(x)\le x^{1/2+(C+3)\varepsilon}+\sum_{\gamma\in\Psi_0\setminus K}|g_\gamma(x)|.$$

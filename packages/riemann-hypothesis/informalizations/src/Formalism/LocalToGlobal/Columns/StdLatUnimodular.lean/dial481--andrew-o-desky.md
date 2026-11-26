---
{
  "module": "src/Formalism/LocalToGlobal/Columns/StdLatUnimodular.lean",
  "declarations": [
    "Formalism.L2.Col.Deco",
    "Formalism.L2.Col.Deco.Ok"
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

## Decorated lattices and auxiliary kernel characters

[Definition / hypothesis ALG.D182](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Deco/)

Hypothesis (decorated kernel lattices). Use ([Arithmetic field models for kernel comparisons](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Fields/)). In this entry write $E,F,K$ for its model fields. For a prime $P$ of $E$, let $O_P=\mathcal O_{E,P}$ and $k_P=\mathcal O_E/P$. Reduction $\operatorname{red}_P:E\to k_P$ is the usual reduction on $O_P$ and zero outside $O_P$. Write $h(x,y)=\sum_i\bar x_i y_i$ on $E^n$.

For finite prime sets $T,G$, a decorated rank-$n$ lattice is a full integral lattice $N\subset E^n$, self-dual for $h$, with maps $f_P:E^n\to k_P$ for $P\in T$ and $b_P:E^n\to k_P^n$ for $P\in G$. Each map is zero outside $N_P$. On $N_P$ it is additive and satisfies $f_P(ax)=\operatorname{red}_P(a)f_P(x)$, respectively $b_P(ax)=\operatorname{red}_P(a)b_P(x)$, for $a\in\mathcal O_E$. Every $f_P$ is nonzero on some vector of $N$. Each $b_P$ maps $N$ onto $k_P^n$, and $x\in N$, $b_P(x)=0$ imply $x\in PN$. A decorated lattice with extra frames at a finite set $Q$ also has $E$-linear isomorphisms $a_P:E^n\simeq E^n$ such that $a_Px\in N_P$ if and only if $x\in O_P^n$.

A residue level at $P$ is a subgroup $H_P\subset\mathrm{GL}_n(k_P)$ with a character $H_P\to K^\times$. An integral local level is a subgroup $H_P\subset\{g\in\mathrm{GL}_n(E):gO_P^n=O_P^n\}$ with a character $H_P\to K^\times$. Families of these levels mean one such choice at each prime of the indicated finite prime set. The top integral level has the entire displayed group and the trivial character.

Let $\mathbb A_{E,f}^{F}=E\otimes_F\mathbb A_{F,f}$ with its integral subring $R=\mathcal O_E\otimes_{\mathcal O_F}\prod_v\mathcal O_{F_v}$. An auxiliary tuple relative to a set $S\subset\mathbb N$ is a character $\xi:(\mathbb A_{E,f}^{F})^\times\to K^\times$ satisfying all the following conditions. It is trivial on diagonal $E^\times$ and embedded $\mathbb A_{F,f}^\times$, has finite order, and kills $1+NR$ in $R^\times$ for some integer $N>0$. At every prime $v$ of $F$ it kills the wild subgroup consisting of integral ideles supported at $v$ and congruent to one modulo the radical of $\ell_vR$. It also kills all integral ideles supported at $v$ unless $v$ splits into two distinct primes of $E$, $Nv$ is prime, $Nv\notin v^2$, and $\ell_v\notin S$.

Define $Q_F(\xi)$ to be the primes where $\xi$ is nontrivial on integral supported ideles. For any map $s$ from primes of $F$ to primes of $E$, define $Q(\xi,s)=s(Q_F(\xi))$ when $Q_F(\xi)$ is finite and the empty set otherwise. Set $B=G\cup Q(\xi,s)$. No condition that $s(v)$ lies above $v$ is implicit in this definition.

A terminal row point is a decorated lattice of rank $N_m-1$ with $T=\varnothing$ and generator set $B$. Its extension at a word $v$ uses $N\oplus\mathcal O_E e_{\rm last}$, functionals $$f_P(x)=\operatorname{red}_P(h(\pi_v e_{\rm last},x)),\qquad b_P(x)=\bigl(b_P(x_{<\rm last}),\operatorname{red}_P(x_{\rm last}/\pi_v)\bigr)$$ on its local lattice, and zero outside it. If these maps do not satisfy all decorated-lattice conditions, the extension is defined to be the standard decorated lattice: $N=\mathcal O_E^{n+1}$, $f_P$ the last-coordinate reduction on $O_P^{n+1}$, and $b_P$ coordinatewise reduction there, with both zero elsewhere.

For decorated lattices $d,d'$ with the same functional-prime set $T$, define $\phi_T(d,d',x)$ to be one if, for every $P\in T$, $xN_P\subseteq N'_P$ and $f'_P(xy)=f_P(y)$ for every $y\in N_P$; otherwise it is zero. A frame lifted from $b_P$ is a fixed $E$-linear isomorphism $a_P$ satisfying $a_P(O_P^n)=N_P$ and $b_P(a_Px)=\operatorname{red}_P(x)$ on $O_P^n$ whenever such an isomorphism exists; an arbitrary fixed isomorphism is used otherwise.

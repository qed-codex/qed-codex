---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/CongFinOddOfLvLac.lean",
  "declarations": [
    "UpperTheory.Gal.Int.Cong.congFinOdd_of_ex",
    "UpperTheory.Gal.Int.Cong.ellSt_holds"
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

## Arbitrarily small subgroups detecting cuspidality

[Theorem REP.1697](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Cong.ellSt_holds/)

Let $E$ be a CM number field, $\ell$ a prime, $a\ge1$, and $w\mid\ell$. Given a neighborhood $N$ of $1$ in $\operatorname{GL}_a(E_w)$ and an integer $m_0\ge0$, there are $m\ge m_0$, a compact open subgroup $J\subset N$, and a surjective homomorphism $$\theta:J\longrightarrow\mathbb Z/\ell^m\mathbb Z$$ with $J$ torsion free. For every nontrivial character $\chi:\mathbb Z/\ell^m\mathbb Z\to\mathbb C^\times$, every smooth irreducible complex representation $\sigma$ of $\operatorname{GL}_a(E_w)$ containing a nonzero vector $v$ with $$\sigma(j)v=\chi(\theta(j))v\qquad(j\in J)$$ is cuspidal.

## l-adic approximation of the Hecke eigenvalues of an automorphic representation of a definite unitary group by those of special representations

[Theorem AGR.1.1775](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Cong.congFinOdd_of_ex/)

Assume ([Hypothesis: l-adic approximation of Hecke eigenvalues with a change of weight at a place above l](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Cong.WtLacEx/)).

Let $E$ be a CM field with maximal totally real subfield $E^+$, let $\ell$ be a prime, let $\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C$ be an isomorphism of fields, and let $a$ be an odd positive integer. Let $\mathcal U$ be the definite unitary group in $a$ variables over $E$. Let $T$ be a finite set of nonsplit finite places of $E$, and let $U$ be an automorphic representation of $\mathcal U$ that is unramified at every nonsplit finite place of $E$ outside $T$. Let $w_0$ and $v'$ be split places of $E$ above $\ell$ with $w_0^+\ne v'^+$.

Then there is a level family $K=(K_w)$ with the following four properties.

1. $U$ has level $K$ away from $w_0$ and $v'$.
2. For every split place $w$ of $E$ with $w^+\ne w_0^+$, the group $K_w$ is open and compact in $GL_a(E_w)$.
3. For every split place $w$ of $E$ with $w^+\ne w_0^+$ and $w^+\ne v'^+$ at which $U$ has a Satake multiset, $K_w=GL_a(\mathcal O_w)$.
4. Let $Z$ and $W$ be finite sets of split places of $E$ such that $U$ has a Satake multiset at every place of $Z\cup W$, every $z\in Z\cup W$ satisfies $z^+\ne w_0^+$ and $z^+\ne v'^+$, and every place of $W$ lies above $\ell$. Then there are nonzero complex numbers $c_{w,n}$, for the finite places $w$ of $E$ and the integers $n$, such that the following two assertions hold for every system of Hecke operators for $K$, with index set $J$, and every system of eigenvalues $\theta=(\theta_j)_{j\in J}$ of $U$ for it.

    

   - (A) For an automorphic representation $U'$ of $\mathcal U$ and a system of eigenvalues $\theta'$ of $U'$ for the same system of Hecke operators, let $\Theta(U',\theta')$ be the family indexed by the disjoint union of $J$ and $W\times\mathbb Z$ with the entry $\theta'_j$ at $j\in J$ and the entry $\iota^{-1}\bigl(c_{w,n}\,s_n(U',w)\bigr)$ at $(w,n)\in W\times\mathbb Z$. Then $\Theta(U,\theta)$ is polynomially approximated by the set of the families $\Theta(U',\theta')$ in which $U'$ is unramified at every nonsplit finite place of $E$ outside $T$, has level $K$ away from $w_0$ and $v'$, is special at $(w_0,v')$, has the weights of $U$ away from $w_0$ and $v'$, and is in general position at every place of $Z\cup W$.
   - (B) If the system of Hecke operators is rational, there is a subfield $L$ of $\overline{\mathbb Q}_\ell$ of finite degree over $\mathbb Q_\ell$ that contains $\theta_j$ for every $j\in J$.

---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/IntegralTwoCocycleReciprocityTrivialAtLastPlaceStatement.lean",
  "declarations": [
    "GlobalTheory.T.integralTwoCocycle_reciprocity_trivial_at_last_place"
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

## Local triviality of an integral two-cocycle at the remaining place

[Theorem GC.0851](https://andrewodesky.com/rh/lean/GlobalTheory.T.integralTwoCocycle_reciprocity_trivial_at_last_place/)

Assume ([Local and global cohomological hypotheses](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.LiteralAutomorphy.LitCoh/)). Let $\ell\ne2$ be prime, let $\Omega$ be an algebraic closure of $\mathbb Q$, and put $G=\operatorname{Gal}(\Omega/\mathbb Q)$. Let $\mathcal O\subseteq\overline{\mathbb Q}_\ell$ be a discrete valuation $\mathbb Z_\ell$-subalgebra finite over $\mathbb Z_\ell$. Let $n\ge0$, let $S$ be a finite set of finite places of $\mathbb Q$ containing the place above $\ell$, and let $N$ be the kernel of the quotient of $G$ unramified outside $S$. Write $\varepsilon$ for the $\ell$-adic cyclotomic character and $$a\equiv_n b\quad\Longleftrightarrow\quad |a-b|_\ell\le|\ell^n|_\ell.$$

Let $\xi:G\times G\to\mathcal O$ be continuous and suppose $$\varepsilon(r)\xi(s,t)+\xi(r,st)\equiv_n\xi(rs,t)+\xi(r,s),$$ $$\xi(sa,tb)\equiv_n\xi(s,t)\qquad(a,b\in N).$$ Fix $v_0\in S$. Suppose that for every $v\in S\setminus\{v_0\}$ one can choose a place of $\Omega$ above $v$ with decomposition group $D_v$, and a function $u_v:G\to\mathcal O$ continuous on $D_v$, such that $$\xi(s,t)\equiv_n\varepsilon(s)u_v(t)-u_v(st)+u_v(s)\qquad(s,t\in D_v).$$ Then for every place of $\Omega$ above $v_0$, with decomposition group $D_{v_0}$, there is a function $u_0:G\to\mathcal O$ continuous on $D_{v_0}$ satisfying the same congruence for all $s,t\in D_{v_0}$.

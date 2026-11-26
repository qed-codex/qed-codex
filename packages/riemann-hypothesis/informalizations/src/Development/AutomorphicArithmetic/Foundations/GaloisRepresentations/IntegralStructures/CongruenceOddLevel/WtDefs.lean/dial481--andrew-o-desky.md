---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/WtDefs.lean",
  "declarations": [
    "UpperTheory.Gal.Int.Cong.GapWt",
    "UpperTheory.Gal.Int.Cong.WtLacEx",
    "UpperTheory.Gal.Int.Cong.WtTo"
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

## Hypothesis: l-adic approximation of Hecke eigenvalues with a change of weight at a place above l

[Definition / hypothesis AGR.D282](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Cong.WtLacEx/)

Let $E$ be a CM field with complex conjugation $c$ and maximal totally real subfield $E^+$, let $\ell$ be a prime, $\iota\colon\overline{\mathbb Q}_\ell\to\mathbb C$ an isomorphism of fields, and $a\ge1$ an integer. Let $\mathcal U$ be the definite unitary group in $a$ variables over $E$, and let $w_0$ and $v'$ be split places of $E$ above $\ell$ with $w_0^+\ne v'^+$. The hypothesis concerns the following data.

- A compact subgroup $K$ of $\mathcal U^\infty$ with these three properties: every $x\in K$ has component $x_u=1$ at every finite place $u$ of $E$ with $u^+=w_0^+$; there is an open neighbourhood $N$ of the identity in $\mathcal U$ such that $K$ contains every $x\in N\cap\mathcal U^\infty$ with $x_u=1$ at every finite place $u$ with $u^+=w_0^+$; and $K$ contains every $x\in\mathcal U_{v'}$ with $x_{v'}\in GL_a(\mathcal O_{v'})$.
- An open subgroup $K_{v'}$ of $GL_a(E_{v'})$. Put $K'=\{x\in K:x_{v'}\in K_{v'}\}$.
- A weight $\lambda_\tau$ for every embedding $\tau\colon E\to\mathbb C$.
- A set $J$, a function $t_j\colon\mathcal U\to\mathbb C$ with finite support for every $j\in J$, and a complex number $\eta(U,j)$ for every complex vector space $U$ of functions on $\mathcal U$ and every $j\in J$.

For a finite place $u$ of $E$ above $\ell$, put $m_u=\sum_\tau\sum_{k=0}^{a-1}|\lambda_{\tau,k}|$, where $\tau$ runs over the embeddings $E\to\mathbb C$ such that $\tau$ or $\tau\circ c$ lies over $u$. Assume the following three conditions.

- (H1) For every $j\in J$ and every $g$ in the support of $t_j$: $g\in\mathcal U^\infty$, and there is an integer $e\ge0$ such that, for every finite place $u$ of $E$ above $\ell$, the matrices $\ell^eg_u$ and $\ell^eg_u^{-1}$ have entries in $\mathcal O_u$, and $$\bigl|\iota^{-1}(t_j(g))\bigr|_\ell\le\ell^{-ae\,m(g)},\qquad m(g)=\sum_{u\mid\ell,\ g_u\ne1}m_u.$$
- (H2) For every $j\in J$ and every $g$ in the support of $t_j$, $g_u=1$ at every finite place $u$ of $E$ with $u^+=w_0^+$ or $u^+=v'^+$.
- (H3) For every automorphic representation $U$ of $\mathcal U$, every $\varphi\in U$ with $R_x\varphi=\varphi$ for all $x\in K'$, and every $j\in J$, $$\sum_{g}t_j(g)\,R_g\varphi=\eta(U,j)\,\varphi.$$

Let $\tau_0\colon E\to\mathbb C$ be an embedding that lies over $v'$, and let $U$ be an automorphic representation of $\mathcal U$ such that $\lambda_\tau$ occurs in $U$ at $\tau$ for every embedding $\tau$ and some nonzero element of $U$ is fixed by $R_x$ for all $x\in K'$.

**Hypothesis.** For all such $E$, $\ell$, $\iota$, $a$, $w_0$, $v'$, $K$, $K_{v'}$, $(\lambda_\tau)$, $J$, $(t_j)$, $\eta$, $\tau_0$ and $U$, the family $\bigl(\iota^{-1}(\eta(U,j))\bigr)_{j\in J}$ is polynomially approximated by the set of the families $\bigl(\iota^{-1}(\eta(U',j))\bigr)_{j\in J}$, where $U'$ runs over the automorphic representations of $\mathcal U$ for which there is a weight $\mu_\tau$ for every embedding $\tau\colon E\to\mathbb C$ with the following four properties:

1. $\mu_\tau=\lambda_\tau$ for every $\tau$ such that neither $\tau$ nor $\tau\circ c$ lies over $v'$;
2. $\mu_{\tau_0}$ is rapidly increasing;
3. $\mu_\tau$ occurs in $U'$ at $\tau$ for every $\tau$;
4. some nonzero element of $U'$ is fixed by $R_x$ for all $x\in K$.

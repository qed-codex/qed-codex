---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/FoundationProofs/LocalCochainsGlueGlobalStatement.lean",
  "declarations": [
    "GlobalTheory.T.local_cochains_glue_global"
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

## Gluing local integral coboundaries modulo a prime power

[Theorem GC.0213](https://andrewodesky.com/rh/lean/GlobalTheory.T.local_cochains_glue_global/)

Assume ([Local and global cohomological hypotheses](https://andrewodesky.com/rh/lean/GlobalTheory.Mem.LiteralAutomorphy.LitCoh/)). Let $\ell\ne2$ be prime, $\Omega$ an algebraic closure of $\mathbb Q$, $G=\operatorname{Gal}(\Omega/\mathbb Q)$, and $O\subset\overline{\mathbb Q}_\ell$ a discrete valuation $\mathbb Z_\ell$-subalgebra finite over $\mathbb Z_\ell$. Let $n\ge0$, let $S$ be a finite set of finite places of $\mathbb Q$ containing the place above $\ell$, and let $N\subset G$ be the kernel of the quotient unramified outside $S$. Write $a\equiv_n b$ for $|a-b|_\ell\le|\ell^n|_\ell$, and let $\varepsilon$ be the $\ell$-adic cyclotomic character.

Let $\xi:G\times G\to O$ be continuous with $$\varepsilon(r)\xi(s,t)+\xi(r,st)\equiv_n\xi(rs,t)+\xi(r,s),\qquad\xi(sa,tb)\equiv_n\xi(s,t)\quad(a,b\in N).$$ Suppose that for each $v\in S$ some place of $\Omega$ above $v$ has decomposition subgroup $D_v$ and an $O$-valued function $u_v:G\to O$, continuous on $D_v$, satisfying $$\xi(s,t)\equiv_n\varepsilon(s)u_v(t)-u_v(st)+u_v(s)\qquad(s,t\in D_v).$$ There is a continuous $u:G\to O$ such that $u(sa)\equiv_n u(s)$ for $a\in N$ and $$\xi(s,t)\equiv_n\varepsilon(s)u(t)-u(st)+u(s)\qquad(s,t\in G).$$

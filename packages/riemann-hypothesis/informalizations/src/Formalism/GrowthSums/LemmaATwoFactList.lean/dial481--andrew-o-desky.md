---
{
  "module": "src/Formalism/GrowthSums/LemmaATwoFactList.lean",
  "declarations": [
    "Formalism.GrowthSums.Top.topCount"
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

## A cardinality bound from marked intervals in a cyclic set

[Theorem ALG.0966](https://andrewodesky.com/rh/lean/Formalism.GrowthSums.Top.topCount/)

Let $n,L_2,K,r,u,M_0,G,N_1\ge0$ be integers with $r,u\ge1$. Put $B=(6r+1)u$ and $b=\lfloor n/B\rfloor$, and suppose $$(M_0+1)B\le n,\qquad(M_0+5)B\le G.$$ Let $T\subseteq\{0,\ldots,n-1\}$. For $i<n$ and $H\ge0$, set $W(i,H)=\{(i+h)\bmod n:0\le h<H\}$. Call the block $[sB,(s+1)B)$ marked if, among its consecutive $6r+1$ subintervals of length $u$, those with odd index are disjoint from $T$ and each with even index meets $T$ in exactly one even integer; subintervals are numbered starting at one. Assume $$\#(T\cap W(i,L_2))\le K,\qquad\#(T\cap W(i,G))\le N_1\qquad(i<n),$$ and suppose that for every $0\le s_0<b$ some $0\le j\le M_0$ makes the block with index $(s_0+j)\bmod b$ marked. Then $$n\le\#T\,G\le N_1(n+G).$$

---
{
  "module": "src/Development/AutomorphicArithmetic/ThickFrames/ThickFrame2Large.lean",
  "declarations": [
    "UpperTheory.BernoulliSumsFrobeniusOrbits.thickFrame2"
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

## Large sets avoiding short three-point relations

[Theorem ALG.1330](https://andrewodesky.com/rh/lean/UpperTheory.BernoulliSumsFrobeniusOrbits.thickFrame2/)

For $e\ge0$, write $H_e=(\mathbb Z/2^{e+2}\mathbb Z)^\times/\langle-1\rangle$, using additive notation for this finite abelian group. There is an absolute $C>0$ with the following property. Fix real numbers $0<\varepsilon<1/52$, $C_0$, and $C_L$. For every sufficiently large real $x$, let $A$ be a finite abelian group of order $N$, equipped with a surjective homomorphism $h:A\to H_e$ and an element $a\in A$ satisfying $$h(ka)=0\Longrightarrow ka=0\qquad(k\in\mathbb Z).$$ Put $n_0=\operatorname{ord}(a)$ and $o=N/n_0$. Let $L\ge2$ be an integer, and assume $$L\le C_L\log x,\qquad o\le C_0,\qquad \tfrac12x^{2+8\varepsilon}\le N\le C_0x^{2+8\varepsilon}.$$ There is a finite set $T\subset\mathbb N$ with $4Ls<n_0$ for every $s\in T$, and no three distinct $s_1,s_2,s_3\in T$ satisfy $$j(s_2-s_1)=i(s_3-s_1)$$ for distinct nonzero integers $i,j$ with $|i|,|j|\le L$. Moreover, $$|T|\ge\frac{n_0}{L}\exp\!\left(-C\sqrt{\log n_0\log L}\right),\qquad |T|\ge x^{-\varepsilon}N,\qquad4L|T|\le n_0.$$

---
{
  "module": "src/Formalism/SizeWindowBrackets/ChainSlopeWindows/PChain.lean",
  "declarations": [
    "Formalism.LFunctionChainParameters.LChain.errX5at_le"
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

## Absorption of the pointwise counting error

[Theorem ANT.0151](https://andrewodesky.com/rh/lean/Formalism.LFunctionChainParameters.LChain.errX5at_le/)

Let $T$ and $W$ be nonempty finite sets, put $r=|T|$, and let $m\in\mathbb N$. Choose real parameters $x,\varepsilon,a,b,b',k,L,\Lambda,B_0,N_c,X'',e_K,K,\bar\delta,\bar\eta,\bar e$, real constants $c_D,c_E,c_H,c_T,c_S,c_Q,c_P,e_D,e_P,c_*$, and real numbers $a_t$ for $t\in T$. Define $$A_0=\sum_{t\in T}a_t,\qquad P_0=c_Prmbx^{e_P\varepsilon},\qquad \Theta=(\bar\eta+4\sqrt{\bar e})x^{c_*}b,$$ $$\mathscr D=c_Dra\Lambda+c_Dm(B_0+N_c)x^{e_D\varepsilon},$$ $$V=2mc_EB_0+c_H(ra\Lambda+mB_0)+A_0c_T\log k,$$ $$K_3=c_Sra\Lambda(2+m/k)+V+c_QmB_0,$$ $$K_0=A_0c_T(\Lambda+m^2\Lambda/k)+\mathscr D+mc_EB_0+c_Sra\Lambda(1+m/k),$$ $$Q_*=c_QP_0+c_Qrm(a/k+b')(c_TmL)+c_QX''+1,\qquad U_*=K_3+Q_*,$$ $$R=K_0+\log|W|+P_0+Q_*+\frac{4(U_*+b)\log(1+x^{c_*})+\Theta}{1-\bar\delta}.$$ Assume all the following conditions:

1. $x\ge1$, $0<\varepsilon\le1$, $b\ge1$, $xb\le a$, $m\le x^{1/2+\varepsilon/2}$, and $xm\le k$.
2. $e_K\ge0$, $1\le k\le x^{e_K}$, $k\le a$, $0\le L,\Lambda\le2x^\varepsilon$, $b'\ge0$, $kb'\le a$, $0\le X''\le a$, and $0\le a_t\le2a$ for every $t\in T$.
3. $B_0,N_c\ge0$, $\log|W|\le(k-3)\log2$, $\bar\delta\le1/2$, and $\bar\eta,\bar e\ge0$.
4. Each of $c_D,c_E,c_H,c_T,c_S,c_Q,c_P$ lies in $[0,K]$, and $e_D,e_P,c_*\ge0$.
5. $\Theta\le Kx^\varepsilon ra$.
6. $\log x\le x^\varepsilon$ and $200(1+K)^2(1+c_*)(1+e_K)\le x^\varepsilon$.

Then $$R\le x^{(e_D+e_P+3)\varepsilon}\left[ra(1+m^2/k)+m(B_0+N_c)\right].$$

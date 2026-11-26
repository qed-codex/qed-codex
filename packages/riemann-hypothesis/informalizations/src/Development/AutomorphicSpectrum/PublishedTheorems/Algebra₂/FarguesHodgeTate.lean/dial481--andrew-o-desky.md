---
{
  "module": "src/Development/AutomorphicSpectrum/PublishedTheorems/Algebra₂/FarguesHodgeTate.lean",
  "declarations": [
    "GlobalTheory.CompanionTheory.Ar.HT.FarguesHodgeTate"
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

## Hodge–Tate maps, orthogonality and a cokernel bound

[Definition / hypothesis PHT.D043](https://andrewodesky.com/rh/lean/GlobalTheory.CompanionTheory.Ar.HT.FarguesHodgeTate/)

**Setup and maps.** Let $p$ be prime, $C$ an algebraically closed field of characteristic zero, and $v:C\to\mathbb R_{\ge0}$ a multiplicative valuation with $v(p)<1$. Let $O$ be a commutative ring with maps $\mathbb Z_p\to O\to C$ identifying $O$ with the valuation ring of $v$, and assume $O$ is complete for the ideal $(p)$.

Let $G$ be a $p$-divisible group over $O$, and let $G^\vee$ be its Cartier dual. For $H=G$ or $G^\vee$, put $$T_pH=\varprojlim_n H[p^n](O),\qquad \omega_H=\varprojlim_n e^*\Omega^1_{H[p^n]/O}.$$ The first inverse limit uses multiplication by $p$; the second uses pullback along the inclusions of the finite group schemes. The symbol $e$ denotes the identity section. Write $\mu_{p^\infty}$ for the $p$-divisible group of $p$-power roots of unity.

Cartier duality associates to $t\in T_pG$ a character $\chi_t:G^\vee\to\mu_{p^\infty}$ and to $s\in T_pG^\vee$ a character $\theta_s:G\to\mu_{p^\infty}$. Their logarithmic differentials are the compatible pullbacks of $dT/T$ on the finite groups of roots of unity. Define $O$-linear maps $$\alpha_G:O\otimes_{\mathbb Z_p}T_pG\longrightarrow\omega_{G^\vee}, \qquad\alpha_G(a\otimes t)=a\,d\log\chi_t,$$ $$\beta_G:O\otimes_{\mathbb Z_p}T_pG^\vee\longrightarrow\omega_G, \qquad\beta_G(a\otimes s)=a\,d\log\theta_s.$$ The first is the linearized Hodge–Tate map. The natural pairing $$e_G:T_pG\times T_pG^\vee\longrightarrow T_p\mu_{p^\infty}$$ is evaluation: its $n$th coordinate at $(t,s)$ is $\theta_{s,n}(t_n)\in\mu_{p^n}(O)$.

**Hypothesis.** For every choice of the objects in this setup, both statements below hold.

1. **Cokernel bound.** For every $\kappa\in O$ satisfying $$\begin{cases} v(\kappa)\le v(4),&p=2,\\ v(\kappa)^{p-1}\le v(p),&p\ne2, \end{cases}$$ one has $\kappa\,\omega_{G^\vee}\subseteq\operatorname{im}\alpha_G$.
2. **Orthogonality.** Choose any sequence $(\zeta_n)_{n\ge0}$ in $O$ with $\zeta_0=1$, $\zeta_{n+1}^p=\zeta_n$ and $\zeta_1\ne1$, and let $\boldsymbol\zeta=(\zeta_n)_n\in T_p\mu_{p^\infty}$. Let $$B:(O\otimes_{\mathbb Z_p}T_pG)\times(O\otimes_{\mathbb Z_p}T_pG^\vee)\longrightarrow O$$ be any $O$-bilinear pairing such that, for every $t\in T_pG$ and $s\in T_pG^\vee$, there is $a\in\mathbb Z_p$ with $$e_G(t,s)=a\boldsymbol\zeta,\qquad B(1\otimes t,1\otimes s)=a,$$ where the second $a$ denotes its image in $O$. Then, for every $x\in O\otimes_{\mathbb Z_p}T_pG$, $$\alpha_G(x)=0\quad\Longleftrightarrow\quad B(x,y)=0\text{ for every }y\in O\otimes_{\mathbb Z_p}T_pG^\vee\text{ with }\beta_G(y)=0.$$

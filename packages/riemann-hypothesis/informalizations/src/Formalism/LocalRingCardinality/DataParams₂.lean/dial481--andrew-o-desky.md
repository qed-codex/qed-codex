---
{
  "module": "src/Formalism/LocalRingCardinality/DataParams₂.lean",
  "declarations": [
    "Formalism.BasicNotions.SizeData₂"
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

## Local size and support data

[Definition / hypothesis PHT.D147](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.SizeData%E2%82%82/)

Hypothesis (local size and support). Use the arithmetic fields, ranks, scale and weight data of ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)). In particular, $K$ is the coefficient number field, $\mu_0$ the distinguished type, $\mu_w$ the type at a finite place $w$ of $K$, and $T\subset A$ the first selected subset. Write $p_w$ for the residue characteristic, $\bar w$ for the conjugate place, and $m$ for the number of stages. Put $$L=x^\varepsilon,\quad b=e^L,\quad a=xb,\quad X'=e^{x^{\varepsilon/3}},\quad b'=a/X',\quad w_0=b'/(xn),\quad X''=a/w_0.$$ Choose a finite set $\mathcal S$ of finite places of $K$, real numbers $$\gamma_{j,w},\ F_{j,w},\ E_{u,j,w},\ \tau_w,\ \iota_w\qquad(j\in\mathbb Z_{\ge0}),$$ a set $\mathcal D\subset\mathbb Z_{\ge0}$ used to discard rational primes, and subsets $T_w\subset T$. Here $u$ runs over the finite nonempty source set of ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)). Its source prime is $T_u$. The five quantities $\gamma_{j,w},F_{j,w},E_{u,j,w},\tau_w,\iota_w$ vanish whenever $w\notin\mathcal S$. Also require $$\gamma_{j,w}=0\quad(p_w\in\{g_0,g_1\}),\qquad T_u\notin\mathcal D,\qquad F_{j,\bar w}=F_{j,w}.$$ The signal and inert prime classes are those of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)). If $p_w$ belongs to neither class, all $\gamma_{j,w}$ and both $\tau_w,\iota_w$ vanish. For $1\le j\le m$, an untwisted place, meaning $\mu_w=\mu_0$, satisfies $$A_{j,w}=F_{j,w}=0,$$ where $A_{j,w}=I_{\mu_w,j,w}+I_{\mu_w,j,\bar w}+J_{\mu_w,j,w}$ in the integer arrays of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)). At every natural stage $j$, require $$p_w>X'',\quad p_w\notin\{g_0,g_1,d\}\quad\Longrightarrow\quad F_{j,w}=0.$$ Require $T_w=T$ if $p_w$ is in the signal class or $p_w\ge X'$. There are real partner weights $w_{j,v,p,e}\ge1$ for every $j,p,e\in\mathbb Z_{\ge0}$ and $v\in T$; their values are identified in ([Orbit weights and local loss definitions](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.Consts/)).

For every source $u$, choose an $\mathcal O_K$-submodule $\widetilde N_u$ in the vector space of its Hermitian source lattice, and rational numbers $\ell_{u,w}$ for its finite places. Write $M_u$ for the inverse image of the initial integral column lattice under the coefficient-space injection of ([Integral forms on column representations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms/)). For family members above the starting scale, if the selected orbit set $\mathcal V_{p_w}$ of ([Orbit weights and local loss definitions](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.Consts/)) is empty and $p_w\ne T_u$, require $\ell_{u,w}=0$.

In a family with external scale $x$ and starting scale $x_1$, impose the following support conditions for $x>x_1$: every place with $p_w\le X''$ lies in $\mathcal S$, and every twisted place lies in $\mathcal S$. All member-scale conditions above use the member's internal scale, which equals $x$ only above $x_1$.

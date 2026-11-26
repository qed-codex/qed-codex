---
{
  "module": "src/Formalism/SharpRestriction/GrowthBounds/DataGChain.lean",
  "declarations": [
    "Formalism.MainNotions.G.Chain",
    "Formalism.MainNotions.G.Fills",
    "Formalism.MainNotions.G.Levels"
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

## Local weight extensions and lattice chains

[Definition / hypothesis PHT.D145](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.GatTies/)

Hypothesis (local weight extensions and lattices). Use the field, rank and source-prime data of ([Local congruence tables](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TwistedPlaces.AdmT/)) and the coefficient places of ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)). A permitted pair $(u,w)$ has residue prime $p=p_w\ge5$, lies in the inert prime class, has even order of the $A$-coordinate of every arithmetic Frobenius at every prime of $E$ above $p$, satisfies $p\notin\mathcal P_{\rm lev}$ and $p\nmid T_u$. For each permitted pair take the initial local polynomial lattice setting of ([Local polynomial lattice settings](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GAtP/)). Write $O_w,K_w$ for its coefficient DVR and fraction field, $v\in\{0,\ldots,c_{\rm cyc}-1\}$ for its local cycles, $n_v$ for their lengths, and $\lambda^0_{v,s}$ for the base dominant integer row at position $s$.

For every permitted pair there is a bijection $$\iota_{u,w}:\coprod_{0\le v<c_{\rm cyc}}\{0,\ldots,n_v-1\}\longrightarrow\Sigma,$$ where $\Sigma$ is the CM type. The base row has length $k$. Every $n_v$ equals the order of the $A$-coordinate of every arithmetic Frobenius $\sigma$ at a prime of $E$ above $p$. If $g(\tau)$ is the Galois label of $\tau\in\Sigma$ relative to the chosen base embedding, then $$g(\iota_{u,w}(v,s+1))=g(\iota_{u,w}(v,s))\,g(\sigma)\,c,$$ where cyclic addition is modulo $n_v$ and $c$ is complex conjugation. At each position, $\lambda^0_{v,s}$ equals the integral coefficient highest-weight row at the initial stage of ([Integral forms on column representations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms/)) under this bijection.

At every cycle choose a subset $T_v\subset\{0,\ldots,n_v-1\}$ and integer functions $a_v,b_v$ on its positions, a natural bound $c_{\rm loc}$, natural numbers $t_{\rm loc},m_{\rm loc}$, and integers $w_{v,j,s}$ for all natural stages $j$. At $s\in T_v$ the endpoints of $\lambda^0_{v,s}$ are $a_v(s),-b_v(s)$ and every interior entry has absolute value at most $c_{\rm loc}$. At $s\notin T_v$, every entry has that bound. Require $$w_{v,1,s}\ge\max\{c_{\rm loc},-\lambda^0_{v,s,k-1}\},\qquad w_{v,j,s}\le w_{v,j+1,s}\quad(j\ge1).$$ For each $j\ge0$ append each of $-w_{v,i,s}$, $1\le i\le j$, exactly $t_{\rm loc}+1$ times to $\lambda^0_{v,s}$. Every resulting row $\lambda^j_{v,s}$ is weakly decreasing.

For each positive stage $j$, choose a finite component set $C_j$ and for every component a level for the rows $\lambda^j_{v,s}$, with the complete meaning of a level in ([Local polynomial lattice settings](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GAtP/)). The initial component set and level are already fixed by ([Local polynomial lattice settings](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GAtP/)). Let $\mathcal F_j$ be the $K_w$-vector space of functions on $C_j$ and tuples of local lattices, with values in the tensor polynomial representation for $\lambda^j$. Its integral module $\mathcal I_j$ is the product over $C_j$ of the specified local integral modules. Choose $K_w$-linear maps $$K_j:\mathcal F_j\longrightarrow\mathcal F_{j+1}\qquad(j\ge0),$$ and an $O_w$-submodule $V^{\rm ram}_{u,w}\subset\mathcal F_0$. Choose also a function $v_{u,w}:A\to\{0,\ldots,c_{\rm cyc}-1\}$.

For family members above the starting scale, identify these local data with ([Orbit weights and local loss definitions](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.Consts/)) as follows. Put $p_0=k^2x^{26}$, $q_j=\{k+(2j-1)(t+1)\}/2$, and let $\mathfrak w_j$, $h_p$, $r_o$, $\mathcal R_p$ be the functions, Frobenius step, orbit-test integer and representatives in ([Orbit weights and local loss definitions](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.Consts/)). Require $$m_{\rm loc}=m,\qquad t_{\rm loc}=t,\qquad c_{\rm loc}\le4S.$$ The local edge-rank parameter of ([Local polynomial lattice settings](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.GAtP/)) is $r_o$ if $p<p_0$, and $1$ otherwise. The restriction of $v_{u,w}$ to $\mathcal R_p$ is injective. A position corresponding under $\iota_{u,w}$ to an embedding with label $(-1,1,h)$ lies outside $T_v$, and $$w_{v,j,s}=\mathfrak w_j(1,h)-q_j\qquad(1\le j\le m).$$ For every $v_0\in\mathcal R_p$, require $n_{v_{u,w}(v_0)}=\operatorname{ord}(h_p)$. At each position $s$ of this cycle, the embedding label is $(1,1,v_0+sh_p)$, and $$s\in T_{v_{u,w}(v_0)}\quad\Longleftrightarrow\quad v_0+sh_p\in T.$$ At selected positions, $a_{v_{u,w}(v_0)}(s)=a_{v_0+sh_p}$ and $b_{v_{u,w}(v_0)}(s)=b_{v_0+sh_p}$. At every position of this cycle, $$w_{v_{u,w}(v_0),j,s}=\mathfrak w_j(0,v_0+sh_p)-q_j\qquad(1\le j\le m).$$

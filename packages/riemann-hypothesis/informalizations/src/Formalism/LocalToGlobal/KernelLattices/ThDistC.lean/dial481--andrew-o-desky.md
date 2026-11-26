---
{
  "module": "src/Formalism/LocalToGlobal/KernelLattices/ThDistC.lean",
  "declarations": [
    "Formalism.L2.Ker.Amb",
    "Formalism.L2.Ker.Seam"
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

## Arithmetic field models for kernel comparisons

[Definition / hypothesis ANT.D184](https://andrewodesky.com/rh/lean/Formalism.L2.Col.Fields/)

Hypothesis (kernel field model). For the arithmetic member of ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), choose number fields $F',E',K'$, an $F'$-algebra structure on $E'$, involutions on $E',K'$, a finite set $\mathcal T'$, and embeddings $e'_\tau:E'\hookrightarrow K'$ for $\tau\in\mathcal T'$. Put $f'=|\mathcal T'|$ and $$E'_q=\{x\in E':e'_\tau(x)=e'_{\tau'}(x)\text{ for all }\tau,\tau'\}.$$ Choose an isomorphism $s:E'\simeq E$, a bijection $t:\mathcal T'\simeq\mathcal T$, and an embedding $\sigma_0:K'\hookrightarrow\mathbb C$ such that $$\sigma_0(e'_\tau(x))=e_{t(\tau)}(s(x)),\qquad s(\bar x)=\overline{s(x)}.$$ For an integral module $N\subset(E')^n$, write $sN$ for the $\mathcal O_E$-span of its coordinatewise image.

Choose a natural number $c$, two natural numbers $g_0,g_1$, elements $\pi_0,\pi_1\in\mathcal O_{E'}$, a finite set $\mathcal W'$, and $T_v\in\mathbb N$, $\pi_v\in\mathcal O_{E'}$ for $v\in\mathcal W'$. Let $G_i$ be the finite set of nonzero prime ideals dividing $\bar\pi_i$, $G=G_0\cup G_1$, and $T(v)$ the finite set dividing $\pi_v$. The finite set of divisors is defined to be empty when the divisor set is infinite. Require, for each $i=0,1$, $$g_i\text{ prime},\quad\pi_i\in E'_q,\quad\pi_i\bar\pi_i=g_i,\quad(\pi_i,\bar\pi_i)=1,\quad |G_i|=f',\quad N P=g_i\ (P\in G_i),\quad g_i\equiv1\pmod c,$$ and require $g_0\ne g_1$. For each $v\in\mathcal W'$, require $$T_v\text{ prime},\quad\pi_v\in E'_q,\quad\pi_v\bar\pi_v=T_v,\quad(\pi_v,\bar\pi_v)=1,\quad |T(v)|=f',\quad NP=T_v\ (P\in T(v)),$$ $$c(g_0g_1)^2\mid\pi_v-1\text{ in }\mathcal O_{E'},\qquad T_v\ne g_0,g_1.$$

At every $P\in G$ choose an additive character $\psi_{0,P}:\mathcal O_{E'}/P\to K'$ and, for each $j=0,\ldots,m-1$, a multiplicative character $\chi_{j,P}:(\mathcal O_{E'}/P)^\times\to(K')^\times$. Also choose values $\mu_{j,P}\in(K')^\times$ and $\eta_P\in(K')^\times$ at every nonzero prime of $E'$. These choices themselves impose no nontriviality or distinctness conditions.

An ambient theta datum consists of an embedding $\sigma_0:K'\hookrightarrow\mathbb C$, scalars $\delta\in\mathbb C$, $d\in\mathbb N$, $h\in\mathbb R$, an integral module $A\subset E'$, numbers $c_\tau\in\mathbb C$, a function $e_{a,b,N,N'}:(\mathcal T'\to M_{b,a}(\mathbb C))\to\mathbb C$ for every $a,b$ and integral modules $N\subset(E')^a,N'\subset(E')^b$, and a scalar $\gamma_{a,b,N,N'}\in\mathbb C$ for every such pair. For the model attached to ([Ideal characters and period lattices](https://andrewodesky.com/rh/lean/Formalism.MainNotions.TaylorLogMetric.Tor/)), these are prescribed by $$h=\operatorname{area}(\Lambda)^{-1},\quad A=\operatorname{span}_{\mathcal O_{E'}}\{s^{-1}(ca):c\in\mathfrak c,\ a\in A_0\},\quad c_\tau=c^D_{t(\tau)},$$ $$e_{a,b,N,N'}(z)=e^{\rm nat}_{a,b,sN,sN'}((z_{t^{-1}(\tau)})_\tau),\qquad\gamma_{a,b,N,N'}=\gamma^{\rm nat}_{a,b,sN,sN'}.$$ Here $e^{\rm nat}$ and $\gamma^{\rm nat}$ are defined in ([Standard period bases for kernel theta functions](https://andrewodesky.com/rh/lean/Formalism.L2.Ker.IsoKG/)); the same $\delta,d$ and $\sigma_0$ are used.

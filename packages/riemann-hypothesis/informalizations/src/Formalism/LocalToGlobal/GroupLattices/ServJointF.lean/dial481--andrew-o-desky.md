---
{
  "module": "src/Formalism/LocalToGlobal/GroupLattices/ServJointF.lean",
  "declarations": [
    "Formalism.L2.G.ServJointF.perToVal2F",
    "Formalism.L2.G.ServJointF.val2AllAtRF"
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

## Transfer of period valuations to column pairings

[Theorem PHT.0138](https://andrewodesky.com/rh/lean/Formalism.L2.G.ServJointF.val2AllAtRF/)

Lower bounds for period valuations extend to bilinear pairings when the test vectors admit integral decompositions.

Let $K$ be a number field with ring of integers $\mathcal O_K$ and an embedding $\iota:K\to\mathbb C$. For a finite place $v$, write $\mathfrak p_v\subset\mathcal O_K$ for its prime ideal and $e_v$ for its ramification index over $\mathbb Q$. Let $\nu_v:K^\times\to\mathbb Z$ be the additive valuation normalized to take value $1$ on a uniformizer at $v$. For $a\in K^\times$, write $\operatorname{ord}_v(a)$ for the exponent of $\mathfrak p_v$ in the principal fractional ideal $(a)=a\mathcal O_K$.

Let $U$ be a finite nonempty index set and $I$ an index set with three distinguished elements $\mu_0,\mu_1,\mu_2$ and an assignment $v\mapsto\mu_v\in I$ for finite places. Fix a coefficient subring $R\subset\mathcal O_K$. For every $\mu\in I$, let $A_\mu$ be a finite-dimensional complex inner product space, let $\pi_\mu:A_\mu\to A_\mu$ be a self-adjoint complex-linear map with $\pi_\mu^2=\pi_\mu$, and put $V^0_\mu=\pi_\mu(A_\mu)$. Choose a finite set $\mathcal G_\mu\subset A_\mu$ spanning $A_\mu$ over $\mathbb C$, and define $$M_\mu=\left\{\sum_{H\in\mathcal G_\mu}\iota(r_H)H:r_H\in R\right\},\qquad \Lambda_\mu=\left\{\sum_{H\in\mathcal G_\mu}\iota(c_H)H:c_H\in\mathcal O_K\right\}.$$ Assume that for every $$\mu\in\{\mu_0,\mu_1,\mu_2\}\cup\{\mu_v:v\text{ a finite place of }K\}$$ and every $Y\in\Lambda_\mu\cap V^0_\mu$, there are a finite set $S\subset M_\mu\cap V^0_\mu$ and coefficients $c_H\in\mathcal O_K$ such that $$Y=\sum_{H\in S}\iota(c_H)H.$$

For every $u\in U$, let $V_u$ be a finite-dimensional $K$-vector space with an $\mathcal O_K$-submodule $\mathcal N_u$. For $u\in U$ and $\mu\in I$, give a period pairing $P_{u,\mu}:V_u\times A_\mu\to\mathbb C$, by which we mean a map such that $H\mapsto P_{u,\mu}(x,H)$ is complex-linear for each $x\in V_u$. For $r\in\mathbb R$, let $\lfloor r\rfloor$ denote the greatest integer at most $r$. Prescribe $\sigma_u(v)\in\mathbb R$ for every $u\in U$ and finite place $v$, and put $$s_u(v)=\lfloor e_v\sigma_u(v)\rfloor\in\mathbb Z.$$ Assume that for every $u\in U$, every finite place $v$, every $x\in\mathcal N_u$ and every $H\in M_{\mu_v}\cap V^0_{\mu_v}$ there is $y\in K$ satisfying $$\iota(y)=P_{u,\mu_v}(x,H),\qquad y=0\ \text{or}\ \nu_v(y)\ge s_u(v).$$

Let $T$ be another index set, with a map $\mu:T\to I$ and an assignment $v\mapsto t(v)\in T$ for finite places. For each $u\in U$, fix a nonnegative integer $a_u$ and a map $J_u:K^{a_u}\to V_u$. For each $t\in T$, fix a nonnegative integer $b_t$, an $\mathcal O_K$-submodule $M_t^{\mathrm{alg}}\subset K^{b_t}$ and a map $E_t:K^{b_t}\to A_{\mu(t)}$. For every $u\in U$ and $t\in T$, give a column pairing, meaning a $K$-bilinear map $Q_{u,t}:K^{a_u}\times K^{b_t}\to K$ on coordinate vectors. Assume:

1. $\mu(t(v))=\mu_v$ for every finite place $v$.
2. $E_t(F)\in V^0_{\mu(t)}$ for every $t\in T$ and $F\in M_t^{\mathrm{alg}}$.
3. $E_t(F)\in\Lambda_{\mu(t)}$ for every $t\in T$ and $F\in M_t^{\mathrm{alg}}$.
4. For every $u\in U$, $t\in T$, $z\in K^{a_u}$ and $F\in K^{b_t}$, $$\iota(Q_{u,t}(z,F))=P_{u,\mu(t)}(J_uz,E_tF).$$

Then, for every $u\in U$ and every $\mathcal O_K$-submodule $N_u\subset K^{a_u}$ with $J_u(N_u)\subset\mathcal N_u$, every finite place $v$, every $z\in N_u$ and every $F\in M_{t(v)}^{\mathrm{alg}}$ satisfy $$Q_{u,t(v)}(z,F)=0\quad\text{or}\quad\operatorname{ord}_v\bigl(Q_{u,t(v)}(z,F)\bigr)\ge s_u(v).$$

## Extension of period valuation bounds to integral spans

[Theorem PHT.0172](https://andrewodesky.com/rh/lean/Formalism.L2.G.ServJointF.perToVal2F/)

Fix the source's arithmetic and column-pairing data over a number field $K$ with embedding $\iota:K\to\mathbb C$. For every source index $u$, let $V_u$ be its period source space and let $J_u:K^{a_u}\to V_u$ be the supplied coordinate map. For each type $\mu$, supply a complex ambient space $A_\mu$, a complex subspace $V^0_\mu$, and a prescribed set $M_\mu$ with finite generating list $\mathcal G_\mu$. Write $P_{u,\mu}:V_u\times A_\mu\to\mathbb C$ for the source's period pairing, complex-linear in its second argument.

For each row index $t$, supply a type $\mu(t)$, an $\mathcal O_K$-submodule $M_t^{\mathrm{alg}}\subset K^{b_t}$, a map $E_t:K^{b_t}\to A_{\mu(t)}$, and $K$-bilinear pairings $Q_{u,t}:K^{a_u}\times K^{b_t}\to K$. Assume the supplied compatibility package: there is a finite-place assignment $v\mapsto t(v)$ with $\mu(t(v))=\mu_v$, where $\mu_v$ is the type assigned to $v$ by the arithmetic data; for every $F\in M_t^{\mathrm{alg}}$, the vector $E_tF$ belongs to $V^0_{\mu(t)}$ and is an $\iota(\mathcal O_K)$-linear combination of $\mathcal G_{\mu(t)}$; and for every $z\in K^{a_u}$ and $F\in K^{b_t}$, $$\iota(Q_{u,t}(z,F))=P_{u,\mu(t)}(J_uz,E_tF).$$

Fix $u,t$, a finite place $v$ of $K$, a real number $s$, and any subset $S\subset K^{a_u}$. Assume that every $\iota(\mathcal O_K)$-linear combination of $\mathcal G_{\mu(t)}$ lying in $V^0_{\mu(t)}$ is a finite $\iota(\mathcal O_K)$-linear combination of elements of $M_{\mu(t)}\cap V^0_{\mu(t)}$. Assume also that, for every $x\in S$ and $H\in M_{\mu(t)}\cap V^0_{\mu(t)}$, there exists $a\in K$ with $$\iota(a)=P_{u,\mu(t)}(J_ux,H),\qquad a=0\ \text{or}\ \nu_v(a)\ge s,$$ where $\nu_v$ is the normalized additive valuation at $v$.

Then, for every $z\in\operatorname{span}_{\mathcal O_K}S$ and every $F\in M_t^{\mathrm{alg}}$, $$Q_{u,t}(z,F)=0\quad\text{or}\quad\operatorname{ord}_v(Q_{u,t}(z,F))\ge s.$$ Here $\operatorname{ord}_v(a)$, for $a\ne0$, is the exponent of the prime associated with $v$ in the principal fractional ideal $(a)$, equal to $\nu_v(a)$. The fixed row index $t$ and place $v$ need not satisfy $t=t(v)$, and $S$ need not be a submodule.

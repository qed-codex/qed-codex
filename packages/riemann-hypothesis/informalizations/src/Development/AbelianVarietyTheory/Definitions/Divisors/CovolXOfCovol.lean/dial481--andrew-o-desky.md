---
{
  "module": "src/Development/AbelianVarietyTheory/Definitions/Divisors/CovolXOfCovol.lean",
  "declarations": [
    "GlobalTheory.CovTop.DeepGoodAt",
    "GlobalTheory.CovTop.GramAt",
    "GlobalTheory.CovTop.SizeAt"
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

## Weight, size and lattice conditions at a unitary lift stage

[Definition / hypothesis ARAK.D242](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.GramAt/)

The following hypotheses specify the weights, numerical bounds and integral lattices used at a unitary lift stage. Use the arithmetic theta data and compatible-point identifications of ([Covolume of integral cusp forms](https://andrewodesky.com/rh/lean/GlobalTheory.CovTop.CovolumeBoundOfX/)). Write $1\le j\le m$ for the stage, $k,m,f,r,n_V$ for the rank parameters, $r=k+m-1$, $(p,q)$ for its moduli signature, $L=x^\varepsilon$, $b=e^L$, and $\Psi=\{\tau:E\hookrightarrow\mathbb C:\tau(\sqrt{-d})=r_0\}$ for the fixed CM type, with the distinguished root $r_0$ of $-d$. Let $(a,n)$ be the stage theta weight, with $a:(\operatorname{Hom}(E,\mathbb C)\times\mathbb N)\to\mathbb N$ and $n\in\mathbb N$.

For $0\le h<r$, define $$\lambda_{\tau,h}=\begin{cases}a(\tau,h)+\lfloor n/2\rfloor,&h<p,\\ -a(\bar\tau,q-1-(h-p))-\lfloor n/2\rfloor,&h\ge p. \end{cases}$$ Put $\alpha_\tau=\lambda_{\tau,k-2}$ when $k-2<r$, and $\alpha_\tau=0$ otherwise; $u_{\tau,h}=\lambda_{\tau,h}-\alpha_\tau$; $\kappa=\sum_{\tau,h}|\lambda_{\tau,h}|$; $d_F=\#\Psi\binom r2$; and $H_{\tau,h}=0$ for $h<p$, $H_{\tau,h}=-1$ for $h\ge p$. Let $c_0$ be the least nonnegative multiple of $8$ at least both $$r+\binom{f p_jq_j+1}{2}+2\quad\hbox{and}\quad8fr+4,$$ where $(p_j,q_j)=(k+j-1,m-j)$ is the prescribed stage signature. Put $$T=\left\lceil P^2d_F^2k/m\right\rceil_+,\qquad z(v)=7\left(\frac{d_F^2}{T}+d_F\rho(v)\right),$$ $$\rho(v)=1-\frac{\prod_\tau\prod_{0\le h<l<r}\bigl((v-3rH)_{\tau,h}-(v-3rH)_{\tau,l}\bigr)}{\prod_\tau\prod_{0\le h<l<r}(v_{\tau,h}-v_{\tau,l})}.$$ All quotients of real numbers have the total convention $a/0=0$.

A quotient weight is an integer array $v$ with $v_{\tau,k-2}=0$ whenever that coordinate exists and with every adjacent gap given by $$v_{\tau,h}-v_{\tau,h+1}=\left\lfloor \frac{u_{\tau,h}-u_{\tau,h+1}+\begin{cases}-c_0-(2r-2),&h+1=p,\\2,&h+1\ne p\end{cases}} {T+d_F+1}\right\rfloor.$$

Hypothesis (size at a stage). For the datum's rational theta exponents $e_{j,\rho}$ at its selected real-place labels $\rho$, define $$E_0=fmbL\log\log x,\qquad t_j=(k+j-1-(m-j))\log\Omega\sum_\rho e_{j,\rho}.$$ There is a specified exponent $A$ such that $$1\le b\le E_0\le x^A b,\quad |t_j|\le x^A b,\quad |t_j|\le P\kappa,\quad b\le P\kappa.$$ If $j<m$, quotient weights exist; for every quotient weight $v$, $$3d_F+5\le T,\qquad0\le\rho(v)<1,\qquad z(v)<1.$$

Hypothesis (Gram norms at a stage). On the rational theta realization, the specified norms at all coefficient embeddings arise from positive definite Hermitian Gram matrices, the full integral lattice $M$ is finitely generated, and $$M\cap\{v:hv=\psi(h)^{-1}v\text{ for every }h\in H_0\}\cap\operatorname{im}e\ne0,$$ where $H_0$, $\psi$ and $e$ are the point's selected finite-level subgroup, its character and its finite-group idempotent acting on the rational theta realization. On the algebraic cusp space of weight $(a,n)$, the Petersson norms have Hermitian Gram matrices, the integral cusp lattice is finitely generated, and its coefficient-field span is the whole cusp space.

Hypothesis (lattices on a cover). On a good cover, the cusp lattices at the four weights $$G,\quad G-W(c_0H,0),\quad G+W(c_0H,0),\quad W(u-c_0H,0)$$ are finitely generated and span their coefficient-field cusp spaces, whose Petersson norms have positive definite Hermitian Gram matrices. Here $G$ has exponent coordinates $a$ and scalar coordinate $n$, and $W$ is defined in ([Constant-norm removal of parallel and scalar weights](https://andrewodesky.com/rh/lean/GlobalTheory.ThinTwist.exists_constant_twist_of_thin_divisor/)). The rank at $G-W(c_0H,0)$ is positive. The component set is finite and nonempty, and the same Gram and full-lattice assertions hold on every component at weight $W(u-c_0H,0)$.

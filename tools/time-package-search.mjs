// Run the existing search-pair workload against the selected package, with controlled per-file delay.
import {spawn} from "node:child_process";
import {localPackage} from "./package-measurements.mjs";

const [directory,seed,database]=process.argv.slice(2);
const server=await localPackage(directory,{cache:true,delay:50});
try {
  const child=spawn(process.execPath,["tools/search-pairs.mjs",server.url,seed,database],{stdio:"inherit"});
  process.exitCode=await new Promise((resolve,reject)=>{child.on("error",reject);child.on("exit",resolve);});
} finally {await server.close();}

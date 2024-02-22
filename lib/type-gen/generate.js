import pkg from 'pg-connection-string'
import kanel from 'kanel'
import kanelZod from 'kanel-zod'

const {parse} = pkg

console.log("Starting...")
console.time("Finished in")

console.log('argv 2'  ,process.argv[2])

const connection = parse(process.argv[2]);

if (!connection) {
    throw new Error("Invalid connection string");
}

/** @type {import('kanel').Config} */
const config = {
    connection: {
        host: connection.host,
        port: connection.port,
        user: connection.user,
        password: connection.password,
        database: connection.database,
    },
    preDeleteOutputFolder: true,
    outputPath: process.argv[3] || "output",

    customTypeMap: {},
    preRenderHooks: [kanelZod.generateZodSchemas],
};

kanel.processDatabase(config).then(() => {
    console.timeEnd("Finished in")
});
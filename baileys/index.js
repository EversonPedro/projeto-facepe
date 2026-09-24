const {
    default: makeWASocket,
    useMultiFileAuthState,
    DisconnectReason
} = require("@whiskeysockets/baileys");

const qrcode = require("qrcode-terminal");

async function conectarWhatsApp() {

    const { state, saveCreds } = await useMultiFileAuthState(
        "auth_info_baileys"
    );

    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: false
    });

    sock.ev.on("connection.update", (update) => {

        const { connection, lastDisconnect, qr } = update;

        // Mostrar QR Code
        if (qr) {
            console.log("\n📱 ESCANEIE ESTE QR CODE PELO WHATSAPP:\n");

            qrcode.generate(qr, {
                small: true
            });
        }

        // Conectado
        if (connection === "open") {
            console.log("\n✅ WHATSAPP CONECTADO COM SUCESSO!");
        }

        // Desconectado
        if (connection === "close") {

            const deveReconectar =
                lastDisconnect?.error?.output?.statusCode !==
                DisconnectReason.loggedOut;

            if (deveReconectar) {
                console.log("🔄 Reconectando...");
                conectarWhatsApp();
            } else {
                console.log("❌ WhatsApp desconectado.");
            }
        }
    });

    // Salvar sessão
    sock.ev.on("creds.update", saveCreds);

    // Receber mensagens
    sock.ev.on("messages.upsert", async ({ messages }) => {

        const mensagem = messages[0];

        if (!mensagem.message) return;

        if (mensagem.key.fromMe) return;

        console.log("\n📩 NOVA MENSAGEM");

        console.log(
            "Número:",
            mensagem.key.remoteJid
        );

        console.log(
            "Mensagem:",
            mensagem.message.conversation || 
            mensagem.message.extendedTextMessage?.text
        );
    });
}

conectarWhatsApp();
document.getElementById("Enkripsi button").addEventListener("click",function()
{const inputteks = document.getElementById("Input teks").value;
    const key = 23;
    const encryptedText = caesarCipher(inputteks, key);
document.getElementById("Output teks").value = encryptedText;
});

function caesarCipher(str,shift) {
    return str.split('').map(char => {
        if (char.match(/[a-z]/i)) {
            const code = char.charCodeAt();
            let shiftedCode = code + shift;

            if (char >= 'a' && char <= 'z') {
                if (shiftedCode > 122) {
                    shiftedCode -= 26;
                }
            } else if (char >= 'A' && char <= 'Z') {
                if (shiftedCode > 90) {
                    shiftedCode -= 26;
                }
            }

            return String.fromCharCode(shiftedCode);
        }
        return char; 
    }).join('');
}
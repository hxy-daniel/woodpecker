var launchpad = require('@cosmjs/launchpad');

// 助记词
// const mnemonic = "dream acquire public come slender shadow toe light dumb helmet affair glory truth flavor turtle try slim lyrics stereo diamond food endless grocery print"

const mnemonic = "canal bar diesel security rude outdoor lumber mountain age moon always truly olympic decorate soda praise dynamic solid street retreat custom bench dune verb"

// 区块链服务器地址
// const lcdApi = "https://1317-white-mole-smuawnad.ws-us03.gitpod.io/";
const lcdApi = "http://123.56.163.105:1317/";

const creator = "cosmos1ewkspdthl53z8rxuwmfnck0nxpfmdl7x27k27f"

// 创建Attribute函数
async function MSGSignAndBroadcast(msg) {
    wallet = await launchpad.Secp256k1HdWallet.fromMnemonic(mnemonic);
    [{ address }] = await wallet.getAccounts();

    client = new launchpad.SigningCosmosClient(lcdApi, address, wallet);
    console.log(address)
    const fee = { "amount": [], "gas": "200000" }
    console.log(await client.signAndBroadcast([msg], fee));
}

// SetAttribute测试
function testSetAttribute(name, idNumber){
    const msg = {
        "type": "woodpecker/SetAttribute",
        "value": {
            "creator": creator,
            "name": name,
            "idNumber": idNumber,
            "address": "CQUPT",
            "job": "Student",
            "nation": "China",
            "hashKey":this.$md5(name+idNumber)
         }
    }
    console.log(this.$md5(name+idNumber))
    MSGSignAndBroadcast(msg)
}

// DeleteAttribute测试
function testDeleteAttribute(){
    const msg = {
        "type": "woodpecker/DeleteAttribute",
        "value": {
            "creator": creator,
            "hashKey":"1111"
         }
    }

    MSGSignAndBroadcast(msg)
}

// SetBodyIndex测试
function testSetBodyIndex(){
    
    const msg = {
        "type": "woodpecker/SetBodyIndex",
        "value": {
            "creator": "cosmos1ewkspdthl53z8rxuwmfnck0nxpfmdl7x27k27f",
            "age": 72,
            "sex": 0,
            "nation": "east",
            "weight": "108.8",
            "height": "182.9",
            "weightIndex": "32.52",
            "obesityWaistline": "1",
            "waistline": "120.5",
            "maxBloodPressure": "125",
            "minBloodPressure": "78",
            "goodCholesterol": "30",
            "batCholesterol": "150",
            "totalCholesterol": "180",
            "Dyslipidemia": "1",
            "pvd": "0",
            "sportActivities": "2",
            "education": "0",
            "marry": 0,
            "income": "0",
            "sourceCase": "clinic",
            "visionBad": "0",
            "drink": "1",
            "highBloodPressure": "1",
            "familialHighBloodPressure": "0",
            "diabetes": "1",
            "familialDiabetes": "1",
            "hepatitis": "1",
            "familialHepatitis": "0",
            "chronicFatigue": "1",
            "alf": "0",
            "hash_key": "02872d6e2853fb495b62624874500589"
          }
    }

    MSGSignAndBroadcast(msg)
}

// DeleteBodyIndex测试
function testDeleteBodyIndex(){
    const msg = {
        "type": "woodpecker/DeleteBodyIndex",
        "value": {
            "creator": creator,
            "hash_key":"daniel"
         }
    }

    MSGSignAndBroadcast(msg)
}

// CreateMedicalHistory测试
function testCreateMedicalHistory(){
    const msg = {
        "type": "woodpecker/CreateMedicalHistory",
        "value": {
            "creator": creator,
            "medicalInstitutionName": "6",
            "diagnosisTime": "6",
            "diagnosisDepartment": "6",
            "diagnosisType": "6",
            "diagnosisDoctor": "6",
            "diagnosisResult": "6",
            "treatmentOptions": "6",
            "hashKey":"daniel"
         }
    }

    MSGSignAndBroadcast(msg)
}

// SetMedicalHistory测试
function testSetMedicalHistory(){
    const msg = {
        "type": "woodpecker/SetMedicalHistory",
        "value": {
            "id":"0",
            "creator": creator,
            "medicalInstitutionName": "6",
            "diagnosisTime": "666666",
            "diagnosisDepartment": "6",
            "diagnosisType": "6",
            "diagnosisDoctor": "6",
            "diagnosisResult": "6",
            "treatmentOptions": "6",
            "hashKey":"daniel"
         }
    }

    MSGSignAndBroadcast(msg)
}

// DeleteMedicalHistory测试
function testDeleteMedicalHistory(){
    const msg = {
        "type": "woodpecker/DeleteMedicalHistory",
        "value": {
            "id":"0",
            "creator": creator,
            "hashKey":"daniel"
         }
    }

    MSGSignAndBroadcast(msg)
}

// testSetAttribute('daniel', '511321199999999990')
// testDeleteAttribute()
testSetBodyIndex()
// testDeleteBodyIndex()
// testCreateMedicalHistory()
// testSetMedicalHistory()
// testDeleteMedicalHistory()

// console.log("user1"+"511321101:",$.md5("user1"+"511321101"))

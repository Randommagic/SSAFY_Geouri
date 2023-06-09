# import time
# import threading
# import asyncio
# import websockets

# async def sendMessage(delay, data):
#     await asyncio.sleep(delay)
#     websockets.send(data)

# async def hello(websocket):

#     # name = await websocket.recv()
#     # print(f"<<< {name}")

#     # greeting = f"Hello {name}!"
#     # await websocket.send(greeting)
#     await sendMessage(5, "woooo")

# async def main():
#     async with websockets.serve(hello, "localhost", 8765):
#         await asyncio.Future()  # run forever

# if __name__ == "__main__":
#     asyncio.run(main())

from websocket import create_connection
import serial
import time

def sendInfo(msg):
    ws = create_connection("ws://localhost:9998")
    ws.send(msg)
    ws.close()


if __name__ == '__main__':

    host = 'localhost'
    user = 'arduino'
    port = 9998

    person_detected = False
    detect_cnt = 0

    py_serial = serial.Serial(
        port='COM3',
        baudrate=9600,
    )

    while True:
        if py_serial.readable():
            # 들어온 값이 있으면 값을 한 줄 읽음 (BYTE 단위로 받은 상태)
            # BYTE 단위로 받은 response 모습 : b'\xec\x97\x86\xec\x9d\x8c\r\n'
            response = py_serial.readline()

            # 디코딩 후, 출력 (가장 끝의 \n을 없애주기위해 슬라이싱 사용)
            distance = float(response[:len(response) - 1].decode())

            print(distance, detect_cnt, person_detected)
            if person_detected is False:
                if distance < 20:
                    detect_cnt = detect_cnt + 1
            else:
                if distance > 20:
                    detect_cnt = detect_cnt + 1

            if detect_cnt > 3:
                if person_detected is False: #newperson
                    sendInfo("newperson")
                else:
                    message = "leave"
                    sendInfo(message)
                person_detected = not person_detected
                detect_cnt = 0
        time.sleep(0.5)
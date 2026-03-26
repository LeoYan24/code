import numpy as np
# 频率检测阈值
threshold = 1000  # 根据实际情况调整
'''DTMF的频率组合，该结构为一个字典结构'''
num = {
    '1': [697, 1209],
    '2': [697, 1336],
    '3': [697, 1477],
    'A': [697, 1633],
    '4': [770, 1209],
    '5': [770, 1336],
    '6': [770, 1477],
    'B': [770, 1633],
    '7': [852, 1209],
    '8': [852, 1336],
    '9': [852, 1477],
    'C': [852, 1633],
    '*': [941, 1209],
    '0': [941, 1336],
    '#': [941, 1477],
    'D': [941, 1633],
}

def getNumWave(numstr,fs,t):
    low_df = 2 * np.pi * num[numstr][0]
    high_df = 2 * np.pi * num[numstr][1]
    discrete_sin1 = np.sin(low_df * t)  # 生成低频部分正弦波
    discrete_sin2 = np.sin(high_df * t)  # 生成高频部分正弦波
    DTMFsin = discrete_sin1 + discrete_sin2  # 组合
    return DTMFsin



def goertzel(data, frequency, sample_rate, num_samples):
    """
    计算给定频率的DFT分量。

    参数:
    data : numpy.ndarray
        输入信号样本。
    frequency : float
        需要计算的频率。
    sample_rate : float
        信号的采样率。
    num_samples : int
        信号的样本数量。

    返回:
    complex
        给定频率的DFT分量。
    """
    omega = 2 * np.pi * frequency / sample_rate
    alpha = 2 * np.cos(omega)
    s1 = s2 = 0.0

    for n in range(num_samples):
        s0 = data[n] + alpha * s1 - s2
        s2, s1 = s1, s0

    # 计算DFT分量
    freq_component = (s1 - np.cos(omega) * s2) * np.exp(1j * omega * (num_samples - 1) / 2)
    return freq_component


def detect_dtmf(data, sample_rate, num_samples):
    """
    检测DTMF信号。

    参数:
    data : numpy.ndarray
        输入信号样本。
    sample_rate : float
        信号的采样率。
    num_samples : int
        信号的样本数量。

    返回:
    str
        检测到的DTMF按键。
    """
    # DTMF频率
    low_freqs = [697, 770, 852, 941]
    high_freqs = [1209, 1336, 1477, 1633]



    # 计算每个频率的DFT分量
    freq_components = {}
    for freq in low_freqs + high_freqs:
        freq_components[freq] = abs(goertzel(data, freq, sample_rate, num_samples))
    print("存在概率:",freq_components)
    # 检测按键
    detected_low = None
    detected_high = None
    for freq in low_freqs:
        if freq_components[freq] > threshold:
            detected_low = freq
            break
    for freq in high_freqs:
        if freq_components[freq] > threshold:
            detected_high = freq
            break

    # 根据检测到的频率组合确定按键
    if detected_low is not None and detected_high is not None:
        if detected_low == 697:
            if detected_high == 1209:
                return '1'
            elif detected_high == 1336:
                return '2'
            elif detected_high == 1477:
                return '3'
            elif detected_high == 1633:
                return 'A'
        elif detected_low == 770:
            if detected_high == 1209:
                return '4'
            elif detected_high == 1336:
                return '5'
            elif detected_high == 1477:
                return '6'
            elif detected_high == 1633:
                return 'B'
        elif detected_low == 852:
            if detected_high == 1209:
                return '7'
            elif detected_high == 1336:
                return '8'
            elif detected_high == 1477:
                return '9'
            elif detected_high == 1633:
                return 'C'
        elif detected_low == 941:
            if detected_high == 1209:
                return '*'
            elif detected_high == 1336:
                return '0'
            elif detected_high == 1477:
                return '#'
            elif detected_high == 1633:
                return 'D'
    return 'No DTMF detected'


# 示例使用
if __name__ == "__main__":
    # 假设我们有一个信号，采样率为8000Hz，包含1209Hz和697Hz的频率成分
    sample_rate = 8000
    num_samples = 1000
    t = np.linspace(0, num_samples / sample_rate, num_samples)
    data = np.sin(2 * np.pi * 1209 * t) + np.sin(2 * np.pi * 697 * t)

    numstr = '9'
    DTMFsin = getNumWave(numstr,sample_rate,t)

    # 使用Goertzel算法检测DTMF信号
    detected_key = detect_dtmf(DTMFsin, sample_rate, num_samples)
    print("Detected DTMF key:", detected_key)

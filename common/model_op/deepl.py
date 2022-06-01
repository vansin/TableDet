from common.app import app, db
from common.models.train_info import TrainInfo
from common.models.eval_info import EvalInfo
import mmcv
import numpy as np

def addTrain(name):

    pass


def addEval(name):
    data_origin = mmcv.load(name)
    epoch = int(name.split('/')[-1].split('_')[1])
    # data_origin['metric'][1]['detail'] = None
    config_name = data_origin['config'].split('/')[-1]
    algorithm = data_origin['config'].split('/')[2]
    dataset = data_origin['config'].split('/')[1]
    checkpoint_size = data_origin['checkpoint_size']

    for iou, eval_detail_result in data_origin['metric'][1].items():
        data = dict()
        data['epoch'] = epoch
        data['dataset'] = dataset
        data['config'] = config_name
        data['algorithm'] = algorithm
        data['checkpoint_size'] = checkpoint_size
        data['iou'] = float(iou)

        detail = eval_detail_result['detail']

        recalls = eval_detail_result['detail'][0]['recall']
        precisions = eval_detail_result['detail'][0]['precision']
        recalls = np.array(recalls)


        precisions = np.array(precisions)
        num_gts = eval_detail_result['detail'][0]['num_gts']
        num_dets = eval_detail_result['detail'][0]['num_dets']
        f1_scores = (2*recalls*precisions)/(recalls+precisions+0.00001)
        f1_scores[np.isnan(f1_scores)] = 0

        if num_dets==0:
            recall_in_max_f1_score = 0
            precision_in_max_f1_score = 0
            max_f1_score = 0
        else:
            max_index = np.argmax(f1_scores)
            recall_in_max_f1_score = recalls[max_index]
            precision_in_max_f1_score = precisions[max_index]
            max_f1_score = f1_scores[max_index]

        eval_detail_result['recall_in_max_f1_score'] = recall_in_max_f1_score
        eval_detail_result['precision_in_max_f1_score'] = precision_in_max_f1_score
        eval_detail_result['max_f1_score'] = max_f1_score

        eval_detail_result['detail'] = None
        data.update(eval_detail_result)
        EvalData(**data)



def TrainData(config, algorithm, dataset, cmd, eval_epoch, epoch):

    q_TrainInfo = TrainInfo.query.filter(
        TrainInfo.algorithm == algorithm,
        TrainInfo.config == config,
        TrainInfo.dataset == dataset
        ).first()

    if q_TrainInfo:

        q_TrainInfo.config = config
        q_TrainInfo.algorithm = algorithm
        q_TrainInfo.dataset = dataset

        q_TrainInfo.cmd = cmd
        q_TrainInfo.eval_epoch = eval_epoch
        q_TrainInfo.epoch = epoch
        # db.session.commit()

    else:

        new = TrainInfo()
        new.config = config
        new.algorithm = algorithm
        new.cmd= cmd
        new.dataset = dataset
        new.eval_epoch = eval_epoch
        new.epoch = epoch

        db.session.add(new)
    
    db.session.commit()



def EvalData(config, epoch, dataset,
    algorithm, iou, detail, ap, num_gts,
    num_dets, recall, precision,
    f1_score,recall_in_max_f1_score,
    precision_in_max_f1_score, max_f1_score, checkpoint_size):

    esp = 0.00001

    q_TrainInfo = EvalInfo.query.filter(
        EvalInfo.epoch == epoch,
        EvalInfo.dataset == dataset,
        EvalInfo.algorithm == algorithm,
        EvalInfo.config == config,
        EvalInfo.iou > iou-esp,
        EvalInfo.iou < iou+esp,
        ).first()

    if q_TrainInfo:

        EvalInfo.epoch = epoch
        EvalInfo.dataset = dataset
        EvalInfo.config = config
        EvalInfo.algorithm = algorithm
        EvalInfo.checkpoint_size = checkpoint_size
        EvalInfo.iou = iou
        # EvalInfo.detail = detail
        EvalInfo.ap = ap
        EvalInfo.num_gts = num_gts
        EvalInfo.num_dets = num_dets
        EvalInfo.recall = recall
        EvalInfo.precision = precision
        # EvalInfo.f1_score = f1_score
        EvalInfo.recall_in_max_f1_score = recall_in_max_f1_score
        EvalInfo.precision_in_max_f1_score = precision_in_max_f1_score
        EvalInfo.max_f1_score = max_f1_score

        # db.session.commit()

    else:
        
        new = EvalInfo()

        new.epoch = epoch
        new.dataset = dataset
        new.config = config
        new.algorithm = algorithm
        new.checkpoint_size = checkpoint_size
        new.iou = iou
        # new.detail = detail
        new.ap = ap
        new.num_gts = num_gts
        new.num_dets = num_dets
        new.recall = recall
        new.precision = precision
        # new.f1_score = f1_score
        new.recall_in_max_f1_score = recall_in_max_f1_score
        new.precision_in_max_f1_score = precision_in_max_f1_score
        new.max_f1_score = max_f1_score

        db.session.add(new)
    
    db.session.commit()

# for row in train_df.itertuples():



#     print(row)

# train_data = pd.pivot_table(train_df, index=['cmd, values=[
#                       'epoch', 'eval_epoch, )

# eval_data = pd.pivot_table(eval_df, index=['cmd, values=[
#     'epoch', 'eval_epoch, )


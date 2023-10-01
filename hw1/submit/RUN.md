# Code Run instructions

## Section 1.2: Behavior Cloning Train Performance

For running training of BC on all 5 environments
```
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Ant.pkl --env_name Ant-v2 --exp_name bc_ant --n_iter 1 --expert_data rob831/expert_data/expert_data_Ant-v2.pkl --video_log_freq -1 --batch_size 5000 --eval_batch_size 5000
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Humanoid.pkl --env_name Humanoid-v2 --exp_name bc_humanoid --n_iter 1 --expert_data rob831/expert_data/expert_data_Humanoid-v2.pkl --video_log_freq -1 --batch_size 5000 --eval_batch_size 5000
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Walker2d.pkl --env_name Walker2d-v2 --exp_name bc_walker2d --n_iter 1 --expert_data rob831/expert_data/expert_data_Walker2d-v2.pkl --video_log_freq -1 --batch_size 5000 --eval_batch_size 5000
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name bc_hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --video_log_freq -1 --batch_size 5000 --eval_batch_size 5000
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/HalfCheetah.pkl --env_name HalfCheetah-v2 --exp_name bc_halfcheetah --n_iter 1 --expert_data rob831/expert_data/expert_data_HalfCheetah-v2.pkl --video_log_freq -1 --batch_size 5000 --eval_batch_size 5000
```

## Section 1.3: Behavior Cloning Eval Performance

For comparing eval performance of BC of Ant-v2 with Humanoid-v2
```
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Ant.pkl --env_name Ant-v2 --exp_name bc_ant --n_iter 1 --expert_data rob831/expert_data/expert_data_Ant-v2.pkl --video_log_freq -1 --batch_size 5000 --eval_batch_size 5000
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name bc_hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --video_log_freq -1 --batch_size 5000 --eval_batch_size 5000
```

## Section 1.4: Hyperparameter tuning for Behavior Cloning

For Hopper-v2, training with different sizes of hidden layers
```
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 10
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 20
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 30
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 40
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 50
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 60
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 70
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 80
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 90
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 100
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 110
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 120
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 130
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 140
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name Hopper --n_iter 1 --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --batch_size 5000 --eval_batch_size 5000 --size 150
```

## Section 2.2: DAgger Running instructions
For Ant-v2
```
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Ant.pkl --env_name Ant-v2 --exp_name dagger_ant --n_iter 10 --do_dagger --expert_data rob831/expert_data/expert_data_Ant-v2.pkl --video_log_freq -1 --eval_batch_size 5000 --batch_size 5000
```

For Hopper-v2
```
python rob831/scripts/run_hw1.py --expert_policy_file rob831/policies/experts/Hopper.pkl --env_name Hopper-v2 --exp_name dagger_hopper --n_iter 10 --do_dagger --expert_data rob831/expert_data/expert_data_Hopper-v2.pkl --video_log_freq -1 --eval_batch_size 5000 --batch_size 5000
```